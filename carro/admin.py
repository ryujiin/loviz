from django.contrib import admin
from models import Carro,LineaCarro

class CarritoAdmin(admin.ModelAdmin):
	list_display=('__unicode__','num_lineas')

class LineaAdmin(admin.ModelAdmin):
	list_display=('id','__unicode__')
			
# Register your models here.
admin.site.register(Carro,CarritoAdmin)
admin.site.register(LineaCarro,LineaAdmin)
