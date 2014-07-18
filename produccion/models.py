from django.db import models
from catalogo.models import Producto
from inventario.models import Materiales

# Create your models here.
class UsoMaterial(models.Model):
	USOS = (
		('capellada','Capellada'),
		('plantilla','Plantilla'),
		('falsa','Falsa'),
		('firme','Firme'),
		('adorno','Adorno'),
	)
	producto = models.ForeignKey(Producto)
	material = models.ForeignKey(Materiales)
	uso = models.CharField(max_length=50,choices=USOS)
	cant_par = models.PositiveIntegerField(default=0)
	cant_doc = models.PositiveIntegerField(default=0)
	costo_doc = models.DecimalField(default=0,max_digits=10, decimal_places=2,null=True)

	def save(self, *args, **kwargs):
		if self.material.unidad_compra=='metro':
			self.cant_doc=self.cant_par*12
			self.costo_doc = self.cant_doc*self.material.precio/self.material.dimenciones
		super(UsoMaterial, self).save(*args, **kwargs)