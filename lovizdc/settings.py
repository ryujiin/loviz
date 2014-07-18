"""
Django settings for lovizdc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5s*+3)im)6&i67==vpm*a1sq_hbh%&hmw=q+ybjpq$&4$h#gsu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #app externas
    'south',
    'easy_thumbnails',
    'rest_framework',
    'stripe',
    'billing',
    #mis app
    'carro',
    'catalogo',
    'cliente',
    'inventario',
    'produccion',
    'orden',
    'tienda',
    'ubigeo',
    'util',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lovizdc.urls'

WSGI_APPLICATION = 'lovizdc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = location("public/media")
MEDIA_URL = '/media/'

STATIC_ROOT = location('public/static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    location('templates'),
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_ALIASES={
    '':{
        'prod_small':{'size':(300,200)},
        'prod_medio':{'size':(600,400)},
        'prod_thum':{'size':(71,53)},
    },
}

SITE_NAME = "Loviz DelCarpio"
SITE_SUBTITULO = "Tienda Oficial de Loviz DelCarpio, Pantuflas y Calzado de calidad para todos los gustos"
META_KEYWORDS = "Pantuflas, Slippers, Pantuflas de Mujer, Pantuflas de Hombres, Pantuflas Loviz, Pantuflas DelCarpio,Scuff, botines, Balerinas,Calzado,Moda"
META_DESCRIPTION = "Sitio Oficial de Loviz DelCarpio, Tenemos las mejores Pantuflas de todo tipo, Scuff, Botines, Balerinas y demas. En distintos Colores y Materiales. Envios a Todo el Peru y si es a Lima es Gratis"
CURRENCY_DEFAULT = 'S/.'

MONEDAS = {
    ('USD','$'),
    ('PEN','S/.'),
}
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'tienda.context_processors.datos_tienda',
    'tienda.context_processors.navegador',
    'tienda.context_processors.navecategorias',
)

#Procesos de Pago

MERCHANT_TEST_MODE = True # Toggle for live
MERCHANT_SETTINGS = {
    "stripe": {
        "API_KEY": "sk_test_CXCoXl4TFl2wHpy2NshOqKch",
        "PUBLISHABLE_KEY": "pk_test_1dnWop5afJiTtiGPo2GsJsa4", # Used for stripe integration
    }
}