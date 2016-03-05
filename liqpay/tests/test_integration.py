# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.html import strip_spaces_between_tags
from django.template import Template, Context
from django.test.client import RequestFactory
from django.conf import settings
from django.test.utils import override_settings
from urllib import urlencode

#from ..models  import UP_ENCODING_MD5, UP_ENCODING_SHA1
from ..integration import LiqPayIntegration
from ..liqpay import ParamValidationError
from ..conf import get_options

from .. import get_liqpay_transaction_model
TransactionModel = get_liqpay_transaction_model()

class LiqPayIntegrationTestCase(TestCase):

    def setUp(self):
        keys = get_options().get('keys')
        self.public_key = keys.get('public_key')
        self.private_key = keys.get('private_key')
        self.liqpay = LiqPayIntegration()

    def test_notify_handler_url_setup(self):
        self.assertEquals(reverse('liqpay_notify_handler'), "/liqpay/notify-handler/")

    def test_get_transaction(self):
        liqpay = LiqPayIntegration()
        data = {
            u'status': [u'sandbox'],
            u'public_key': [u'i18196708214'],
            u'description': [u'\u041f\u043b\u0430\u0442\u0435\u0436 \u0437\u0430 PRO \u0430\u043a\u043a\u0430\u0443\u043d\u0442'],
            u'order_id': [u'order#8'],
            u'liqpay_order_id': [u'3495616u1427260695433822'],
            u'currency': [u'UAH'],
            u'amount': [u'150.00'],
            u'version': [u'2'],
            u'receiver_commission': [u'4.13'],
            u'signature': [u'RSqW/KKcJDa61HSFZwtCP9vTYWE='],
            u'sender_phone': [u'380973356702'],
            u'type': [u'buy'],
            u'transaction_id': [u'53641640']
        }
        records = TransactionModel.objects.all()
        self.assertEqual(len(records),0)

        rf = RequestFactory()
        post_data, trans, result = liqpay.get_transaction(rf.post(path=reverse('liqpay_notify_handler'), data=data))
        self.assertEqual(result, 'CREATED')

        records = TransactionModel.objects.all()
        self.assertEqual(len(records),1)

    # def test_notify_handler_with_invalid_data(self):
    #     data = {
    #         'payment': u'amt=2000.00&ccy=UAH&details=\u0421\u043f\u043b\u0430\u0442\u0430 \u0437\u0430 \u043f\u0438\u0442\u0430\u043d\u043d\u044f: \u0422\u0435\u0441\u0442\u043e\u0432\u0435 \u043f\u0438\u0442\u0430\u043d\u043d\u044f&ext_details=&pay_way=privat24&order=1&merchant=100000&state=test&date=160114183814&ref=test payment&sender_phone=+380888888888&payCountry=UA',
    #         'signature': '7df61c288b9245cf8d1d021256fa4074646ec7de',
    #     }
    #     p24 = Privat24Integration()
    #     rf = RequestFactory()
    #     post_data, trans, result = p24.get_transaction(rf.post(path=reverse('privat24_notify_handler'), data=data))
    #     self.assertEqual(result, 'FAIL')
