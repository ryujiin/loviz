from django.conf.urls import patterns, include, url
from views import ProductoCategoriaList,ProductoDetallesView


urlpatterns = patterns('',
    url(r'^(?P<categoria_slug>[\w-]*)_(?P<pk>\d+)/$',
			ProductoCategoriaList.as_view(),name='catalogo_categoria'),
    url(r'^producto/(?P<producto_slug>[\w-]*)_(?P<pk>\d+)/$',
			ProductoDetallesView.as_view(),name='catalogo_producto'),
)