from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'efit_prod',
        'USER': 'efit_prod',
        'PASSWORD': 'BCYNRc644RnY',
        'HOST': '',
        'PORT': '',
    }
}

DEFAULT_FROM_EMAIL = u"noreply@english-i.com"
ALLOWED_HOSTS = ['english-i.com']

STATIC_ROOT = os.path.abspath(root_path('..', '..', 'static'))
MEDIA_ROOT = os.path.abspath(root_path('..', '..', 'media'))
