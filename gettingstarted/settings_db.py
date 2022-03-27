import os
import dj_database_url
import django_on_heroku
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {}

DATABASES['default'] = dj_database_url.config(config('DATABASE_URL'))
django_on_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }