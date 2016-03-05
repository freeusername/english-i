# Django settings for efit project.
import os

PROJ_MODULE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.normpath(os.path.join(PROJ_MODULE_ROOT, ".."))
root_path = lambda *args: os.path.join(ROOT, *args)
path = lambda *args: os.path.join(PROJ_MODULE_ROOT, *args)

APPEND_SLASH = True

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = u"default-from-email"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)


# Optional. If you want to use redirects, set this to True
SOLID_I18N_USE_REDIRECTS = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = root_path('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path('static'),
)

LOCALE_PATHS = (
    path('locale'),
    #    root_path('business/locale'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7nd^f2b1oh2()ta2q5-gduc-kgd8%+q2d7*(@dpxi92q!-k%&k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'pages.middleware.PageFallbackMiddleware',
    # Uncomment the next line if installed i18n:
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'efit.urls'

LOGIN_URL = '/login/'

AUTH_USER_EMAIL_UNIQUE = True
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_ACTIVATION_DAYS = 21
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.auth_backends.EmailBackend',
)
REGISTRATION_AUTO_LOGIN = False

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'efit.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'menu.context_processors.menu',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'registration',
    'imagekit',
    'tinymce',
    'filebrowser',
    'djlime',
    'modeltranslation',
    'liqpay',
    # bundled apps
    'core.utils',
    'core.configs',
    'core.metatags',
    'accounts',
    'pages',
    'courses',
    'slides',
    'testimonials',
    'orders',
    'invoices',
    'payments',
    'menu',
)

TINYMCE_FILEBROWSER = True

TINYMCE_DEFAULT_CONFIG = {
    "theme_advanced_buttons1": "bold, italic, underline, strikethrough, sub, sup, separator, forecolor, backcolor, separator, justifyleft, justifycenter, justifyright, justifyfull",
    "theme_advanced_buttons1_add": "formatselect, fontselect, fontsizeselect, separator, bullist, numlist",
    "theme_advanced_buttons2": "hr, separator, undo, redo, separator, link, unlink,  anchor,  image, media, cleanup, code",
    "theme_advanced_buttons2_add": "tablecontrols, separator, moveforward, movebackward, absolute, styleprops",
    "theme_advanced_buttons3": "",
    "extended_valid_elements": "hr[class|width|size|noshade], font[face|size|color|style], span[class|align|style]",
    'theme': "advanced",
    # 'content_css': ','.join([os.path.join(STATIC_URL, p) for p in [
    #     'css/text_pages.css'
    # ]]),
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'forced_root_block': 'p',
    'plugins': "style, layer, table, advhr, advimage, advlink, emotions, insertdatetime, media, searchreplace, contextmenu, paste, directionality, inlinepopups, wordcount",
    'theme_advanced_fonts': "Arial=arial,helvetica,sans-serif;Courier New=courier new,courier,monospace;Georgia=georgia,times new roman,times,serif;Tahoma=tahoma,arial,helvetica,sans-serif;Times New Roman=times new roman,times,serif;Verdana=verdana,arial,helvetica,sans-serif;Impact=impact;WingDings=wingdings;Andale Mono=andale mono,times;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Trebuchet MS=trebuchet ms,geneva;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats;Century Gothic=century gothic",
    'width': "700",
    'height': "300",
    'font_size_style_values': "8pt, 10pt, 12pt, 14pt, 18pt, 24pt, 36pt, 48pt, 52pt, 64pt, 72pt, 86pt, 92pt",
    # 'font_size_classes': "",
    # 'font_size_legacy_values': "1, 2, 3, 4, 5, 6, 7, 8",
    'theme_advanced_font_sizes': "8pt, 10pt, 12pt, 14pt, 18pt, 24pt, 36pt, 48pt, 52pt, 64pt, 72pt, 86pt, 92pt",
}

# Privat24 setting
LIQPAY_TRANSACTION_MODEL = 'payments.payment'
LIQPAY_OPTIONS = {
    'keys': {
        'public_key': 'i84284097998',
        'private_key': 'kbcOpJ8NBPM9cNuLi2welYmuCVwxo5WXXJmiypuN',
    },
    'defaults': {
        'currency': 'UAH',
        'language': 'ru',
        'sandbox': 0,
        # 'pay_way':    ('card', 'liqpay', 'delayed', 'invoice', 'privat24'),
        'type': 'buy',
        'result_url': 'http://english-i.com/profile/payments/complete/',
        'server_url': 'http://english-i.com/liqpay/notify-handler/',
    },
}


# filebrowser settings
FILEBROWSER_PATH_TINYMCE = path(STATIC_ROOT, '/tiny_mce/')
FILEBROWSER_URL_TINYMCE = STATIC_URL + '/tiny_mce/'
FILEBROWSER_PATH_FILEBROWSER_STATIC = path(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_URL_FILEBROWSER_STATIC = STATIC_URL + 'filebrowser/'
FILEBROWSER_VERSIONS_BASEDIR = 'thumbnails/'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],  # Enter in folder
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.docx', '.xlsx'],
}


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ROOT + "/log/app.log",
            'maxBytes': 0,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'error_logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ROOT + "/log/error.log",
            'maxBytes': 0,
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'error_logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'app': {
            'handlers': ['logfile', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

