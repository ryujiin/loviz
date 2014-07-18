import datetime
from django.core.exceptions import ObjectDoesNotExist

from django.db import models
from lovizdc import settings
from django.utils.translation import ugettext_lazy as _
from catalogo.models import *
from django.contrib.auth.models import User as User

# Create your models here.
class Carro(models.Model):
	ABIERTO, FUCIONADA, GUARDADA, CONGELADA, ENVIADA = (
        "Abierto", "Fusionada", "Guardado", "Congelado", "Enviado")
	ESTADO_ELECCION = (
        (ABIERTO, _("Abierto - Actualmente activa  ")),
        (FUCIONADA, _("Fusionada - sustituida por otra canasta ")),
        (GUARDADA, _("Guardado - para los articulos para comprar mas adelante ")),
        (CONGELADA, _("Congelado - la canasta no se puede modificar ")),
        (ENVIADA, _("Enviado - ha sido ordenado en la caja")),
    )
	propietario = models.ForeignKey(User,related_name='Carrito', null=True,blank=True)
	sesion_carro = models.CharField(max_length=120,blank=True,null=True)
	estado = models.CharField(max_length=128,default=ABIERTO,choices=ESTADO_ELECCION)
	date_created = models.DateTimeField(auto_now_add=True)
	date_submitted = models.DateTimeField(blank=True,null=True)
	
	def __unicode__(self):
		return "Carro de %s" %(self.propietario)

	def all_lineas(self):
		return LineaCarro.objects.filter(carro=self)

	def num_lineas(self):
		return self.all_lineas().count()

	def save(self, *args, **kwargs):
		self.date_submitted = datetime.datetime.now()
		super(Carro, self).save(*args, **kwargs)

class LineaCarro(models.Model):
	carro = models.ForeignKey(Carro,related_name="lineas")
	producto = models.ForeignKey(Producto,blank=True,null=True)
	variacion = models.ForeignKey(ProductoVariacion,blank=True,null=True)
	cantidad = models.PositiveIntegerField(default=1)
	date_created = models.DateTimeField(auto_now_add=True)

	def get_precio(self):
		precio = self.variacion.precio_minorista
		if self.variacion.oferta > 0:
			oferta = precio*self.variacion.oferta/100
			precio = precio-oferta
		return precio

	def __unicode__(self):
		return "linea de %s con %s articulos de %s" %(self.carro.propietario,self.cantidad,self.variacion)

	def save(self, *args, **kwargs):
		try:
			coincidencias = LineaCarro.objects.get(carro=self.carro,variacion=self.variacion)
		except ObjectDoesNotExist:
			super(LineaCarro, self).save(*args, **kwargs)
		else:
			coincidencias.delete()
			self.cantidad = coincidencias.cantidad+self.cantidad
			super(LineaCarro, self).save(*args, **kwargs)
