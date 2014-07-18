from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from ubigeo.models import Ubigeo

# Create your views here.
class IndexTemplate(TemplateView):
	template_name = "layout3.html"

	def get_context_data(self, **kwargs):
	    context = super(IndexTemplate, self).get_context_data(**kwargs)

class CheckoutVista(TemplateView):
	template_name = "carro/checkout.html"

	def get_context_data(self, **kwargs):
	    context = super(CheckoutVista, self).get_context_data(**kwargs)
	    context['regiones'] = Ubigeo.objects.filter(parent=None).order_by('name')
	    return context