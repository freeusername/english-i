# -*- coding: utf-8 -*-
from django.test import TestCase
from decimal import Decimal

from ..signals import update_order
from ..utils import order2json, get_password
from ..crypto import encrypt
from .. import models
from liqpay.models import LIQPAY_STATUS_SANDBOX
from .factories import PaymentFactory, PaymentOrderFactory
from accounts.tests.factories import UserFactory
from accounts.models import User


class UpdateOrderTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.save()
        self.order = PaymentOrderFactory.build(
            user=self.user,
            backend=models.BACKEND_LIQPAY,
            sum=Decimal('150.00')
        )
        self.order.save()
        # self.order = models.PaymentOrder.objects.get(pk=self.order.pk)
        order_json = order2json(self.order)
        order_crypted = encrypt(get_password(), order_json)
        self.payment = PaymentFactory.build(
            order_id=order_crypted,
            amount=Decimal('150.00'),
            status=LIQPAY_STATUS_SANDBOX
        )
        self.payment.save()

    def test_update_order(self):
        self.assertEqual(self.user.is_premium, False)

        update_order(self.payment)

        order = models.PaymentOrder.objects.get(pk=self.order.pk)
        self.assertEqual(order.transaction, self.payment)

        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.is_premium, True)





