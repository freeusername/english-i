from decimal import Decimal
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserCourse
from core.configs.models import AppConfig


INVOICE_NOPRICE = 'invoice_noprice'
INVOICE_NOTPAID = 'invoice_notpaid'
INVOICE_PAID = 'invoice_paid'

INVOICE_STATUS_VALUE = (
    (INVOICE_NOPRICE, _('No price')),
    (INVOICE_NOTPAID, _('Not paid')),
    (INVOICE_PAID, _('Paid')),
)


class Invoice(models.Model):
    user = models.ForeignKey('accounts.User', related_name='invoice_user', verbose_name='user')
    course = models.ForeignKey(UserCourse, related_name='invoice_course', verbose_name='course')
    status = models.CharField(_('status'), max_length=255, choices=INVOICE_STATUS_VALUE, default=INVOICE_NOPRICE, editable=False)
    price = models.DecimalField(_('price'), default=0, max_digits=20, decimal_places=2)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return _("Invoice #%s") % self.pk

    @property
    def get_title(self):
        return self.__unicode__

    @property
    def get_price_ru(self):
        price_ru = self.price * AppConfig.objects.get(key='currency_rate', enabled=True).value
        price_ru = Decimal("{0:.2f}".format(price_ru))
        return price_ru

    def save(self, *args, **kwargs):
        if self.price >= 0 and self.status == 'invoice_noprice':
            self.status = 'invoice_notpaid'
        elif self.price == 0 and self.status != 'invoice_noprice':
            self.status = 'invoice_noprice'
        super(Invoice, self).save(*args, **kwargs)

    def get_invoice_description(self):
        if self.course.course.title:
            course_title = self.course.course.title
        else:
            course_title = 'Custom course %s' % self.course.course.pk
        return _("Payment for course '%s'") % course_title

    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoices')


def decode_sum(sum):
    return Decimal(sum)