from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^',CarroList.as_view(),name='mi-bolsa'),
)