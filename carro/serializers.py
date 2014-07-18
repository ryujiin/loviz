from rest_framework import serializers
from models import LineaCarro,Carro

class LineaSerializer(serializers.ModelSerializer):
	talla = serializers.SerializerMethodField('get_talla')
	nombre = serializers.SerializerMethodField('get_full_name')
	total_linea = serializers.SerializerMethodField('get_precio_varia')
	imagen = serializers.SerializerMethodField('get_imagen')
	precio = serializers.SerializerMethodField('get_precio')
	class Meta:
		model = LineaCarro
		fields = ('id','carro','producto','variacion','cantidad','nombre','talla','total_linea','imagen','precio')

	def get_talla(self,obj):
		return obj.variacion.talla

	def get_full_name(self,obj):
		return obj.producto.full_name

	def get_precio_varia(self,obj):
		return round(float(obj.get_precio()*obj.cantidad),2)

	def get_precio(self,obj):
		return round(float(obj.get_precio()),2)

	def get_imagen(self,obj):
		return obj.producto.get_thum2_producto

class CarroSerializer(serializers.ModelSerializer):
	#lineas = serializers.PrimaryKeyRelatedField(many=True,read_only=False)
	lineas = LineaSerializer(many=True,read_only=False)
	total_carro = serializers.SerializerMethodField('get_total_carro')
	num_items = serializers.SerializerMethodField('get_items')
	class Meta:
		model = Carro
		fields = ('id','propietario','estado','lineas','total_carro','num_items')

	def get_total_carro(self,obj):
		lineas = obj.all_lineas();
		total = 0
		for linea in lineas:
			precio = linea.get_precio()
			total = total+(precio*linea.cantidad)
		return round(float(total),2)

	def get_items(self,obj):
		lineas = obj.all_lineas();
		num = 0
		for linea in lineas:
			num = num+linea.cantidad
		return num
