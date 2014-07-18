from rest_framework import serializers
from models import *

class ImgProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductoImagen
		fields =('url','producto','foto','thum','thum_small','thum_medio')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):	
	imagenes_producto = ImgProductoSerializer(many=True)
	class Meta:
		model = Producto
		fields =('url','nombre','categorias','nombre_mostrar','slug','imagenes_producto')

