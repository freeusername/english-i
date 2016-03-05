# coding: UTF-8
from . import app_settings
from . import models

def get_options():
    options = {
        'keys': {
            'public_key': '',   # Must be set in settings.py
            'private_key': '',  # Must be set in settings.py
            'host': 'https://www.liqpay.com/api/',
        },
        'defaults': {
            'version': models.API_VERSION,
            'result_url': '',   # Must be set in settings.py
            'server_url': '',   # Must be set in settings.py
            'currency': models.LIQPAY_CCY_UAH,
            'sandbox': 1,
            'language': 'ru',
            'type': models.LIQPAY_TYPE_BUY,
        },

    }
    settings_opts = {}
    try:
        settings_opts = app_settings.LIQPAY_OPTIONS
    except AttributeError:
        pass
    if settings_opts:
        keys = settings_opts.get('keys')
        if keys:
            options['keys'].update(keys)
        defaults = settings_opts.get('defaults')
        if defaults:
            options['defaults'].update(defaults)
    return options

