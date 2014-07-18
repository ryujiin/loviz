from django.conf.urls import patterns, include, url
import settings
from tienda.views import IndexTemplate,CheckoutVista


from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from catalogo import views as viewsCatalogo
from carro import views as viewsCarro

router = routers.DefaultRouter()
router.register(r'productos', viewsCatalogo.ProductoViewsets)
router.register(r'categorias',viewsCatalogo.CategoriaViewsets)
router.register(r'imagenesprod',viewsCatalogo.ImagenesProductViewsets)
router.register(r'carros',viewsCarro.CarroViewSet)
router.register(r'lineas',viewsCarro.LineaCarroViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lovizdc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),    
    url(r'^$', IndexTemplate.as_view(), name='home'),
    url(r'^json/carro/$',viewsCarro.CarritoViewsApi.as_view()),
    url(r'^json/carro/(?P<pk>[0-9]+)/$',viewsCarro.CarritoDetailViews.as_view()), 

    url(r'^catalogo/', include('catalogo.urls')),
    url(r'^mi-bolsa/', include('carro.urls')),
    url(r'^checkout/$',CheckoutVista.as_view(),name='checkout'),
    url(r'^ubigeo/', include('ubigeo.urls')),
    url(r'zebra/', include('zebra.urls', namespace="zebra", app_name='zebra')),
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns