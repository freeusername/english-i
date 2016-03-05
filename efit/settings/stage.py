from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'efit_dev',
        'USER': 'efit_dev',
        'PASSWORD': 'AqQr7KYnMz4e',
        'HOST': '',
        'PORT': '',
    }
}

DEFAULT_FROM_EMAIL = u"noreply@efit.freshlimestudio.com"
ALLOWED_HOSTS = ['efit.freshlimestudio.com']

STATIC_ROOT = os.path.abspath(root_path('..', '..', 'static'))
MEDIA_ROOT = os.path.abspath(root_path('..', '..', 'media'))
