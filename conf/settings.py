"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import environ
from pathlib import Path
from datetime import timedelta

env = environ.Env(DEBUG=(bool, False))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q7#r(xwsit^1g=kv78#*qd$kk^6kshxvdl5x_^^97=_0kqm^7('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django_extensions',
  'rest_framework',
  'users',
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

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

'''
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}
'''

DATABASES = {
  'default': {
    'ENGINE': 'mysql.connector.django',
    'NAME': env('DJANGO_DB_NAME', default='flutter-tutorials-backend'),
    'USER': env('DJANGO_DB_USERNAME', default='root'),
    'PASSWORD': env('DJANGO_DB_PASSWORD', default=''),
    'HOST': env('DJANGO_DB_HOST', default='127.0.0.1'),
    'PORT': env('DJANGO_DB_PORT', default='3306'),
    'OPTIONS': {'charset': 'utf8mb4',},
  }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 사용자 인증 모델을 users.User 로 사용하겠다!!
AUTH_USER_MODEL = 'users.User'

JWT_AUTH = {
  'JWT_SECRET_KEY': SECRET_KEY,
  'JWT_AUTH_HEADER_PREFIX': 'Bearer',
  # 토큰 새로 고침 기능을 활성화합니다
  'JWT_ALLOW_REFRESH': False,
  'JWT_ALGORITHM': 'HS512',
  # 토큰 만료 시간 설정
  'JWT_VERIFY_EXPIRATION': True,
  'JWT_EXPIRATION_DELTA': timedelta(days=5)
}

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
  'DEFAULT_AUTHENTICATION_CLASSES': ('conf.authentication.JWTAuthentication',),
  'NON_FIELD_ERRORS_KEY': 'error',
  'DEFAULT_PAGINATION_CLASS': 'conf.pagination.CustomPagination',
  'PAGE_SIZE': 20,
  'DEFAULT_RENDERER_CLASSES': (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
  ),
}