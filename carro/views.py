import json
from django.shortcuts import render
from models import Carro,LineaCarro
from ubigeo.models import Ubigeo

from serializers import CarroSerializer,LineaSerializer
from django.http import HttpResponse, Http404
from django.views.generic.base import TemplateView

class CarroList(TemplateView):
	template_name = "carro/carro.html"

# vistas de la API
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CarritoViewsApi(APIView):

	def get(self,request,format=None):
		if request.user.is_authenticated():
			carro = Carro.objects.filter(propietario= request.user,estado='Abierto').order_by('-date_submitted')[:1]
			serializer = CarroSerializer(carro,many=True)
			return Response(serializer.data)
		elif 'coockie_carro' in request.COOKIES:
			coockie_carro = request.COOKIES["coockie_carro"]
			carro = Carro.objects.filter(sesion_carro=coockie_carro,estado='Abierto').order_by('-date_submitted')[:1]
			serializer = CarroSerializer(carro,many=True)
			return Response(serializer.data)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format=None):
		serializer = CarroSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

class CarritoDetailViews(APIView):

	def get_object(self,pk):
		try:
			return Carro.objects.get(pk=pk)
		except Carro.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		carro = self.get_object(pk)
		serializer = CarroSerializer(carro)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		carro = self.get_object(pk)
		serializer = CarroSerializer(carro,data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		
class CarroViewSet(viewsets.ReadOnlyModelViewSet):
	model = Carro
	serializer_class = CarroSerializer

class LineaCarroViewSet(viewsets.ModelViewSet):
	model = LineaCarro
	serializer_class = LineaSerializer

	def get_queryset(self):
		carro = 0
		if self.request.user.is_authenticated():
			carro = Carro.objects.filter(propietario = self.request.user,estado='Abierto').order_by('-date_submitted')[:1]
		return LineaCarro.objects.filter(carro = carro)