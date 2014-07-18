from django.db import models

# Create your models here.
class Color(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Talla(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class TipoFirme(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class TipoMaterial(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class TipoCorte(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre