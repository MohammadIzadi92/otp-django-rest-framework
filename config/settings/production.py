from .base import *


ALLOWED_HOSTS = ['82.115.19.155', 'localhost']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("POSTGRES_NAME"),
        'USER': config("POSTGRES_USER"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
