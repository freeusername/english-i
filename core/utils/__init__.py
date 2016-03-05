# -*- coding: utf-8 -*-
default_app_config = 'core.utils.apps.UtilsConfig'

import logging
logger = logging.getLogger('django.request')

class TranslationTabsMixin(object):

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
