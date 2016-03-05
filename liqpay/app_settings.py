# -*- coding: utf-8 -*-
import os
from django.conf import settings

from . import models

LIQPAY_TRANSACTION_MODEL = getattr(settings, 'LIQPAY_TRANSACTION_MODEL', 'liqpay.liqpaytransaction')

default_options = {
    'keys': {
        'public_key': 'i18776700000',
        'private_key': 'TNWPlCopK0FAmmxqPxv8KKtrY5bqcifCjaGefC8K',
    },
    'defaults': {
        'currency': models.LIQPAY_CCY_UAH, # валюта
        'sandbox': 1,
        'type': models.LIQPAY_TYPE_BUY,
        'language': 'ru',
        'result_url':'http://example.com/payments/return/', #страница, принимающая клиента после оплаты
        'server_url':'http://example.com/liqpay/notify-handler/', #страница, принимающая ответ API о результате платежа
    },
}
if hasattr(settings, 'LIQPAY_OPTIONS'):
    setted_options =  getattr(settings, 'LIQPAY_OPTIONS')
    if setted_options:
        LIQPAY_OPTIONS = setted_options
    else:
        LIQPAY_OPTIONS = default_options
else:
    LIQPAY_OPTIONS = default_options
