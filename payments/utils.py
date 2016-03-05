#-*- coding: utf-8 -*-
import json

class FraudAttemptError(Exception):
    #
    # def __init__(self, *args, **kwargs): # real signature unknown
    #     pass
    #
    # @staticmethod # known case of __new__
    # def __new__(S, *more): # real signature unknown; restored from __doc__
    #     pass
    pass


def order2json(order):
    return (json.dumps({'pk': order.pk, 'datetime': order.created_at.strftime('%Y%m%d%H%M%S'), 'sum': str(order.sum)}))

def get_password():
    from django.core.exceptions import ImproperlyConfigured
    from django.conf import settings
    try:
        options = settings.LIQPAY_OPTIONS
        keys = options.get('keys')
        if not keys:
            raise ImproperlyConfigured("Option LIQPAY_OPTIONS['keys'] must be set in your settings.py file.")
        password = keys.get('private_key')
        if not password:
            raise ImproperlyConfigured("Option LIQPAY_OPTIONS['keys']['private_key'] must be set in your settings.py file.")
        return password[:32]
    except AttributeError:
        raise ImproperlyConfigured("Option LIQPAY_OPTIONS must be set in your settings.py file.")


def get_order(order_crypted):
    from .crypto import decrypt
    from .models import PaymentOrder
    order_json = decrypt(get_password(), order_crypted)
    try:
        order_dict = json.loads(order_json)
    except ValueError:
        raise FraudAttemptError("Invalid order hash")
    order_id = order_dict.get('pk')
    order = None
    try:
        order = PaymentOrder.objects.get(pk=int(order_id))
    except PaymentOrder.DoesNotExist:
        pass
    return order, order_json
