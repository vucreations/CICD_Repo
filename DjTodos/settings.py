"""
Django settings for DjTodos project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ

from DjTodos.loggers import FILE_LOGGING

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o_0ymkuf71@mk=&8&qrxjlpjt7%t-&lvf62^v+z(r597_f#*3i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "vite_integration",
    "todos",
    "contacts",
    "rest_framework",
    "drf_yasg",
    "swagger",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DjTodos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DjTodos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE", default="django.db.backends.sqlite3"),
        "USER": env("DB_USER", default="postgres"),
        "PASSWORD": env("DB_PASSWORD", default="postgres"),
        "NAME": env("DB_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


INTERNAL_IPS = [
    "127.0.0.1",
]


############################  React related stuff ####################
# FRONTEND_DIR: point it to the folder your vite app is in.

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend/src")
FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, "frontend/dist")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# You may change these, but it's important that the dist folder is includedself.
# If it's not, collectstatic won't copy your bundle to production.

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    FRONTEND_BUILD_DIR,
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = "staticfiles/"

LOGIN_URL = "/admin/login/"

LOGGING = FILE_LOGGING


################## Celery Settings ########################

BROKER_URL = 'redis://localhost:6379'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE


