import dj_database_url
import django_on_heroku

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

DATABASES = {}

DATABASES['default'] = dj_database_url.config()
django_on_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']