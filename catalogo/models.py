from django.db import models
from util.models import Color,Talla
from django.template.defaultfilters import slugify
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Producto(models.Model):
	MARCAS = (
    ('Loviz DelCarpio', 'Loviz DelCarpio'),
    ('Doomckan DC', 'Doomckan DC'),
)
	nombre = models.CharField(max_length=120,blank=True,null=True)
	full_name = models.CharField(max_length=120, unique=True,blank=True,null=True,editable=False)
	nombre_mostrar = models.CharField(max_length=120, unique=True,blank=True,null=True,editable=False)
	marca = models.CharField(max_length=120, choices=MARCAS)
	categorias = models.ManyToManyField('Categoria',blank=True,null=True)
	color = models.ForeignKey(Color,blank=True,null=True)
	slug = models.CharField(max_length=120,editable=False)
	parientes = models.ManyToManyField('self',blank=True,null=True)
	activo = models.BooleanField(default=True)
	descripcion = models.TextField(blank=True,null=True)
	meta_descripcion = models.CharField(max_length=200,blank=True,null=True)
	meta_keyword = models.CharField(max_length=250,blank=True,null=True)

	def __unicode__(self):
		return self.full_name

	def save(self, *args, **kwargs):
		if not self.nombre_mostrar:
			self.nombre_mostrar = '%s %s, %s' %(self.nombre,self.color,self.marca)
		if not self.slug:
			self.slug = slugify(self.nombre_mostrar)
		self.full_name = ("(%s) %s") %(self.color,self.nombre)
		super(Producto, self).save(*args, **kwargs)

	def get_thum_producto(self):
		imagen = ProductoImagen.objects.get(producto=self,orden=0)
		foto_thum = imagen.thum
		return foto_thum

	def get_thum2_producto(self):
		imagen = ProductoImagen.objects.get(producto=self,orden=0)
		foto_thum2 = imagen.thum_small
		return foto_thum2

	def get_imagenes(self):
		imgs = ProductoImagen.objects.filter(producto=self)
		return imgs

	def get_imagen(self):
		img = ProductoImagen.objects.get(producto=self,orden=0)
		return img

	def get_variacion_precio(self):
		variaciones = ProductoVariacion.objects.filter(producto=self).order_by('-oferta')
		if not variaciones:
			variaciones = ProductoVariacion.objects.filter(producto=self).order_by('precio_minorista')
		return variaciones

	@models.permalink
	def get_absolute_url(self):
		return ('catalogo_producto', (), { 'producto_slug': self.slug ,'pk': self.pk})

class Categoria(models.Model):
	nombre = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120,unique=True,editable=False)
	descripcion = models.TextField(blank=True,null=True)
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='categories',blank=True,null=True,max_length=250)
	full_name = models.CharField(max_length=255,db_index=True, editable=False)
	padre = models.ForeignKey("self",blank=True,null=True,verbose_name="Padre")
	meta_descripcion = models.CharField(max_length=200,blank=True,null=True)
	meta_keyword = models.CharField(max_length=250,blank=True,null=True)
	posicion = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.full_name

	def update_slug(self,commit=True):
		slug_separator = '-'
		full_name_separator = ' > '
		padre=self.padre
		slug = slugify(self.nombre)
		if padre:
			self.slug = ("%s%s%s") %(padre.slug,slug_separator,slug)
			self.full_name = ("%s%s%s") %(padre.full_name,full_name_separator,self.nombre)
		else:
			self.slug = slug
			self.full_name = self.nombre
		if commit:
			self.save()

	@models.permalink
	def get_absolute_url(self):
		return ('catalogo_categoria', (), { 'categoria_slug': self.slug ,'pk': self.pk})

	def save(self,update_slugs=True, *args, **kwargs):
		if update_slugs:
			self.update_slug(commit=False)
		try:
			match = self.__class__.objects.get(slug=self.slug)
		except self.__class__.DoesNotExist:
			pass
		else:
			if match.id != self.id:
				raise ValidationError(
					("A category with slug '%(slug)s' already exists") % {'slug': self.slug})
		if self.padre:
			self.posicion=self.padre.posicion+1
		super(Categoria, self).save(*args, **kwargs)

	def get_hijos(self):
		hijos = Categoria.objects.filter(padre=self)
		return hijos


class ProductoImagen(models.Model):
	producto = models.ForeignKey(Producto,related_name="imagenes_producto")
	foto = ThumbnailerImageField(upload_to="catalogo/producto/imagen/")
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	orden = models.PositiveIntegerField(default=0)
	thum = models.CharField(max_length=250,blank=True,null=True)
	thum_small = models.CharField(max_length=250,blank=True,null=True)
	thum_medio = models.CharField(max_length=250,blank=True,null=True)

	def save(self, *args, **kwargs):
		imagenes = ProductoImagen.objects.filter(producto=self.producto).count()
		if not self.orden:
			if not imagenes == 0:
				self.orden = imagenes
		self.thum = get_thumbnailer(self.foto)['prod_thum'].url
		self.thum_small = get_thumbnailer(self.foto)['prod_small'].url
		self.thum_medio = get_thumbnailer(self.foto)['prod_medio'].url
		super(ProductoImagen, self).save(*args, **kwargs)

class ProductoVariacion(models.Model):
	producto = models.ForeignKey(Producto)
	talla = models.ForeignKey(Talla)
	precio_minorista = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	oferta = models.PositiveIntegerField(default=0)
	
	def save(self, *args, **kwargs):
		super(ProductoVariacion, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s S/.%s, oferta %s" %(self.producto.nombre,self.precio_minorista,self.oferta)

	def en_oferta(self):
		precio = self.precio_minorista
		if self.oferta:
			descuento = self.precio_minorista*self.oferta/100
			precio = self.precio_minorista-descuento
		return precio

class Atributo(models.Model):
	nombre = models.CharField(max_length=100,blank=True,null=True)

class AtributoValor(models.Model):
	atributo = models.ForeignKey(Atributo)
	valor = models.CharField(max_length=100)
    