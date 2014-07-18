from django.db import models
from util.models import TipoMaterial,TipoFirme,Color,Talla

# Create your models here.
class Materiales(models.Model):
	UNIDAD = (
    ('metro', 'Metro'),
    ('paquete', 'Paquete'),
    ('unidad', 'Unidad'),
    )
	nombre = models.CharField(max_length=150)
	tipo = models.ForeignKey(TipoMaterial,blank=True,null=True)
	color = models.ForeignKey(Color,blank=True,null=True)
	unidad_compra = models.CharField(max_length=100,choices=UNIDAD,blank=True,null=True)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True)
	dimenciones = models.PositiveIntegerField(default=0)
	imagen = models.ImageField(upload_to="imagenes/material/",null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.nombre

class Firme(models.Model):
	tipo = models.ForeignKey(TipoFirme)
	color = models.ForeignKey(Color)
	talla = models.ForeignKey(Talla)
	precio = models.DecimalField(max_digits=10,decimal_places=2,null=True)
	cantidad = models.PositiveIntegerField(default=0)
	alarma = models.PositiveIntegerField(default=20)

	def alarma_senal(self):
		return self.alarma < self.cantidad
	alarma_senal.boolean = True

	def valor_total(self):
		valor = self.precio*self.cantidad
		return "s/.%s" %valor

	def __unicode__(self):
		return "%s (%s)" %(self.color,self.talla)