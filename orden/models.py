from django.db import models
from django.conf import settings
from carro.models import Carro
from django.contrib.auth.models import User
from cliente.models import Direccion

# Create your models here.
class Orden(models.Model):
	ESTADO = (
		('1','Esperando Pago'),
		('2','Cancelado'),
		('3','Enviado'),
		('4','Pago Aceptado'),
		('5','Error de pago'),
		('6','Devuelto'),
	)
	numero = models.CharField(max_length=128,db_index=True)
	carro = models.ForeignKey(Carro,null=True,blank=True)
	usuario = models.ForeignKey(User,blank=True,null=True)
	modena = models.CharField(max_length=120,default=settings.CURRENCY_DEFAULT)
	total = models.DecimalField(decimal_places=2, max_digits=12)
	gasto_envio = models.DecimalField(decimal_places=2,max_digits=12)
	direccion_envio = models.ForeignKey(Direccion,blank=True,null=True)
	metodo_envio = models.CharField(max_length=100,blank=True,null=True)
	fecha_compra = models.DateTimeField(auto_now_add=True, db_index=True)
	estado = models.CharField(max_length=100,choices=ESTADO)

	class Meta:
		verbose_name = 'Orden'
		verbose_name_plural = 'Ordenes'    