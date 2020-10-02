"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='h=xs689usahtj4k97n!x7qh*i2p)=t$#626a*6d^av)yrtdb&2')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'base',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'import_export',

    # GeoDjango
    'django.contrib.gis',

    # Django-leaft
    'leaflet',
    'djgeojson',

    # Apps
    'domain.imovel.apps.ImovelConfig',
    'domain.localizacao.apps.LocalizacaoConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.db('DB_DEFAULT', default=f'psql://app:app@localhost:54321/app')
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


PUBLIC_DIR = BASE_DIR / 'static'

STATIC_ROOT = PUBLIC_DIR / 'collect'
STATIC_URL = '/static/collect/'

MEDIA_ROOT = PUBLIC_DIR / 'media'
MEDIA_URL = '/static/media/'

STATICFILES_DIRS = (
    PUBLIC_DIR / 'geral',
)

# Configuration import-export
IMPORT_EXPORT_USE_TRANSACTIONS = True


LEAFLET_CONFIG = {
    'TILES': [('GStreets', 'http://www.google.cn/maps/vt?lyrs=m@189&gl=cn&x={x}&y={y}&z={z}',
               {'attribution': '&copy; Google'}),
              ('GSatellite',
               'http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}',
               {'attribution': '&copy; Google'})]
}
