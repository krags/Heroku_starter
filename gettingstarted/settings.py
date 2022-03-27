from .settings_aws import *
#from .settings_db import *
import os
from decouple import config
import django_on_heroku
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR -> ', BASE_DIR)

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

#ALLOWED_HOSTS = ['','keithragsdale.com']
ALLOWED_HOSTS = ['keithragsdale.com']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "hello",
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

ROOT_URLCONF = "gettingstarted.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "gettingstarted.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE" : "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3")
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Heroku Logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'MYAPP': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }
# }


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

print(BASE_DIR)
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#added last ->
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Database setup
# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(config('DATABASE_URL'))
# django_on_heroku.settings(locals())
#del DATABASES['default']['OPTIONS']['sslmode']
#del DATABASES['default']['sslmode']

