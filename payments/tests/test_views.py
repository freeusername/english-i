# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from decimal import Decimal

from ..utils import order2json, get_password
from ..crypto import encrypt
from .. import models
from liqpay.models import LIQPAY_STATUS_SANDBOX, LIQPAY_CCY_UAH
from liqpay.integration import LiqPayIntegration
from .factories import PaymentFactory, PaymentOrderFactory
from accounts.tests.factories import UserFactory
from accounts.models import User

class ServerViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.save()
        self.order = PaymentOrderFactory.build(
            user=self.user,
            backend=models.BACKEND_LIQPAY,
            sum=Decimal('150.00')
        )
        self.order.save()
        order_json = order2json(self.order)
        order_crypted = encrypt(get_password(), order_json)
        liqpay = LiqPayIntegration({
            'sandbox': 1
        })
        self.payment_attributes = {
            'status': 'sandbox',
            'public_key': liqpay._public_key,
            'description': 'Test payment 1',
            'order_id': order_crypted,
            'liqpay_order_id': '3495616u1427211195433822',
            'currency': LIQPAY_CCY_UAH,
            'amount': Decimal('150.00'),
            'version': '2',
            'receiver_commission': [u'4.13'],
            'signature': '',
            'sender_phone': '380971234567',
            'type': 'buy',
            'transaction_id': '53444440'
        }
        signature = liqpay.res_signature(self.payment_attributes)
        self.payment_attributes['signature'] = signature

    def test_server_view(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.is_premium, False)

        resp = self.client.post(reverse('liqpay_notify_handler'), data=self.payment_attributes)
        self.assertEqual(resp.status_code, 200)

        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.is_premium, True)
