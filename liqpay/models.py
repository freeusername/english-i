# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

API_VERSION = "3"

LIQPAY_CCY_UAH = 'UAH'
LIQPAY_CCY_USD = 'USD'
LIQPAY_CCY_EUR = 'EUR'
LIQPAY_CCY_RUB = 'RUB'

LIQPAY_CCY_CHOICES = (
    (LIQPAY_CCY_UAH, _('UAH')),
    (LIQPAY_CCY_USD, _('USD')),
    (LIQPAY_CCY_EUR, _('EUR')),
    (LIQPAY_CCY_RUB, _('RUB')),
)

LIQPAY_TYPE_BUY = 'buy'
LIQPAY_TYPE_DONATE = 'donate'
LIQPAY_TYPE_CHOICES = (
    (LIQPAY_TYPE_BUY, _('Buy')),
    (LIQPAY_TYPE_DONATE, _('Donate')),
)

LIQPAY_STATUS_SUCCESS = 'success'               # успешный платеж
LIQPAY_STATUS_FAILURE = 'failure'               # неуспешный платеж
LIQPAY_STATUS_WAIT_SEQURE = 'wait_secure'       # платеж на проверке
LIQPAY_STATUS_WAIT_ACCEPT = 'wait_accept'       # Деньги с клиента списаны, но магазин еще не прошел проверку
LIQPAY_STATUS_WAIT_LC = 'wait_lc'               # Аккредитив. Деньги с клиента списаны, ожидается подтверждение доставки товара
LIQPAY_STATUS_PROCESSING = 'processing'         # Платеж обрабатывается
LIQPAY_STATUS_SANDBOX = 'sandbox'               # тестовый платеж
LIQPAY_STATUS_SUBSCRIBED = 'subscribed'         # Подписка успешно оформлена
LIQPAY_STATUS_UNSUBSCRIBED = 'unsubscribed'     # Подписка успешно деактивирована
LIQPAY_STATUS_REVERSED = 'reversed'             # Возврат клиенту после списания


class AbstractLiqpayTransaction(models.Model):
    version = models.CharField(_('version'), max_length=32)
    public_key = models.CharField(_('public key'), max_length=32)
    amount = models.DecimalField(_('amount'), max_digits=16, decimal_places=2)
    currency = models.CharField(_('currency'), max_length=32)
    description = models.CharField(_('description'), max_length=128)
    order_id = models.CharField(_('order id'), max_length=255)
    pay_type = models.CharField(_('payment type'), max_length=32, default=LIQPAY_TYPE_BUY, blank=True)
    transaction_id = models.CharField(_('transaction id'), max_length=128, null=True, blank=True)
    sender_phone = models.CharField(_('sender phone'), max_length=32, null=True, blank=True)
    status = models.CharField(_('status'), max_length=32)

    signature = models.TextField(_('signature'))
    raw_data = models.TextField(_('raw data'), null=True, blank=True)

    class Meta:
        verbose_name = _('liqpay transaction')
        verbose_name_plural = _('liqpay transactions')
        abstract = True

    def __unicode__(self):
        return _('Transaction #(%s)') % self.order_id


class LiqpayTransaction(AbstractLiqpayTransaction):

    class Meta:
        swappable = 'LIQPAY_TRANSACTION_MODEL'




