import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


from liqpay.models import AbstractLiqpayTransaction
from liqpay.signals import transaction_was_successful as liqpay_transaction_was_successful
from .signals import liqpay_transaction_successfull

from invoices.models import Invoice

BACKEND_ADMIN = 'admin'
BACKEND_LIQPAY = 'liqpay'

BACKEND_CHOICES = (
    (BACKEND_ADMIN, 'Admin'),
    (BACKEND_LIQPAY, 'LiqPay'),
)

class PaymentOrder(models.Model):
    transaction_type = models.ForeignKey(ContentType, related_name='payment_orders', blank=True, null=True,)
    transaction_id = models.PositiveIntegerField(blank=True, null=True,)
    transaction = generic.GenericForeignKey('transaction_type', 'transaction_id',)

    user = models.ForeignKey('accounts.User', verbose_name=_('user'), related_name='payment_orders')
    invoice = models.ForeignKey(Invoice, verbose_name=_('invoice'), related_name='payment_orders', null=True, blank=True)
    sum = models.DecimalField(_('sum'), max_digits=16, decimal_places=2, default=0)

    backend = models.CharField('bakend', max_length=32, default=BACKEND_ADMIN, choices=BACKEND_CHOICES)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True, editable=False)

    class Meta:
        ordering = ['-id']
        verbose_name = _('payment order')
        verbose_name_plural = _('payment orders')


class Payment(AbstractLiqpayTransaction):

    created_at = models.DateTimeField(_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('payment')
        verbose_name_plural = _('payments')


liqpay_transaction_was_successful.connect(liqpay_transaction_successfull, dispatch_uid="efit.payments.models")