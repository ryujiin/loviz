from django.db import models
from ubigeo.models import *
from django.contrib.auth.models import User

# Create your models here.
class Direccion(models.Model):
	pais = models.CharField(max_length=100)
	direccion = models.CharField(max_length=255)
	distrito_peru = models.ForeignKey(Ubigeo,blank=True,null=True)
	usuario = models.ForeignKey(User,blank=True,null=True)
	invitado = models.CharField(max_length=100,blank=True,null=True)