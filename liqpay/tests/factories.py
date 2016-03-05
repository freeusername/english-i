# -*- coding: utf-8 -*-
import factory
from django.utils import timezone
from decimal import Decimal

from .. import get_liqpay_transaction_model
from ..  import models
TransactionModel = get_liqpay_transaction_model()

class LiqPayTransactionFactory(factory.Factory):
    FACTORY_FOR = TransactionModel
    version = models.API_VERSION
    public_key = ''
    amount = Decimal("123.45")
    currency = models.LIQPAY_CCY_UAH
    description = 'Test payment'
    order_id = factory.Sequence(lambda n: 'order_{0}'.format(n))

    signature = 'signature'
