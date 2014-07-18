from catalogo.models import Categoria
from django.conf import settings
from django.core.urlresolvers import reverse

def datos_tienda(request):
	return {
		"titulo_web":settings.SITE_NAME,
		"titulo_tagline":settings.SITE_SUBTITULO,
		"meta_keyword":settings.META_KEYWORDS,
		"meta_description":settings.META_DESCRIPTION,
		"moneda":settings.CURRENCY_DEFAULT,
		"request": request,
	}

def navegador(request):
	cat = Categoria.objects.all()
	menu = {'menu': [
		{'name': 'Inicio', 'url':'/'},
		{'name':'novedades','url':'/'},
	]}
	return menu

def navecategorias(request):
	categorias = Categoria.objects.filter(posicion=0)
	return {'categorias':categorias}

