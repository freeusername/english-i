# -*- coding: utf-8 -*-
import factory
from django.utils import timezone
from decimal import Decimal

from ..models import Payment, PaymentOrder
from liqpay import models

class PaymentFactory(factory.Factory):
    FACTORY_FOR = Payment
    version = models.API_VERSION
    public_key = ''
    amount = Decimal("123.45")
    currency = models.LIQPAY_CCY_UAH
    description = 'Test payment'
    order_id = factory.Sequence(lambda n: 'order_{0}'.format(n))

    signature = 'signature'

class PaymentOrderFactory(factory.Factory):
    FACTORY_FOR = PaymentOrder

    sum = Decimal("123.45")




