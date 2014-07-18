from django.contrib import admin
from models import *
from produccion.models import UsoMaterial

# Register your models here.
class ProductoImagenInline(admin.TabularInline):
	model = ProductoImagen
	exclude =('thum','thum_small','thum_medio',)

class VariacionInline(admin.TabularInline):
	model = ProductoVariacion

class UsoMaterialInline(admin.TabularInline):
	model=UsoMaterial

class ProductoAdmin(admin.ModelAdmin):
	inlines = [ProductoImagenInline,VariacionInline,UsoMaterialInline]
	filter_horizontal = ('parientes','categorias')
	list_display = ('id','foto_producto','full_name',"nombre",'nombre_mostrar')

	def foto_producto(self, obj):
		url = obj.get_thum_producto()
		tag = '<img src="%s">' % url
		return tag
	foto_producto.allow_tags = True

class CategoriaAdmin(admin.ModelAdmin):
	list_display=('nombre','__unicode__','slug','get_hijos')

class ProductoVariacionAdmin(admin.ModelAdmin):
	list_display = ('id','__unicode__')
		
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(ProductoVariacion,ProductoVariacionAdmin)
