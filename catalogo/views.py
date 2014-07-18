from django.shortcuts import render,get_object_or_404
from models import *
from django.views.generic import TemplateView,ListView,DetailView

class ProductoCategoriaList(ListView):
	context_object_name = "productos"
	template_name = "catalogo/categoria2.html"

	def get_queryset(self):
		if 'pk' in self.kwargs:
			self.categoria = get_object_or_404(Categoria, pk=self.kwargs['pk'])
		return Producto.objects.filter(categorias=self.categoria).distinct()

	def get_context_data(self, **kwargs):
	    ctx = super(ProductoCategoriaList, self).get_context_data(**kwargs)
	    ctx['categoria'] = self.categoria
	    return ctx

class ProductoDetallesView(DetailView):
	template_name = "catalogo/detalle_producto2.html"
	context_object_name= "producto"
	model = Producto

# vistas de la API
from rest_framework import viewsets
from serializers import ProductoSerializer,ImgProductoSerializer
# Create your views here.

class ProductoViewsets(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoSerializer

class CategoriaViewsets(viewsets.ModelViewSet):
	model = Categoria

class ImagenesProductViewsets(viewsets.ModelViewSet):
	model = ProductoImagen
	serializer_class = ImgProductoSerializer
