from django.core.exceptions import ImproperlyConfigured
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from .liqpay import LiqPay, to_unicode

from .conf import get_options
from .forms import LiqpayBackForm
from . import models
import logging

from .signals import transaction_was_successful

from payments.utils import get_order
from payments.models import PaymentOrder

csrf_exempt_m = method_decorator(csrf_exempt)
never_cache_m = method_decorator(never_cache)
require_POST_m = method_decorator(require_POST)

from . import get_liqpay_transaction_model

TransactionModel = get_liqpay_transaction_model()

logger = logging.getLogger('app')


class LiqPayIntegration(LiqPay):
    display_name = "LiqPay"

    def __init__(self, params=None):
        # read settings options
        settings_options = get_options()
        keys = settings_options.get('keys')
        if not keys:
            raise ImproperlyConfigured("Option LIQPAY_OPTIONS['keys'] must be set in your settings.py file.")
        public_key = keys.get('public_key')
        if not public_key:
            raise ImproperlyConfigured(
                "Option LIQPAY_OPTIONS['keys']['public_key'] must be set in your settings.py file.")
        private_key = keys.get('private_key')
        if not private_key:
            raise ImproperlyConfigured(
                "Option LIQPAY_OPTIONS['keys']['private_key'] must be set in your settings.py file.")
        host = keys.get('host')
        if not host:
            raise ImproperlyConfigured("Option LIQPAY_OPTIONS['keys']['host'] must be set in your settings.py file.")
        defaults = settings_options.get('defaults')
        if not defaults:
            raise ImproperlyConfigured("Option LIQPAY_OPTIONS['defaults'] must be set in your settings.py file.")
        super(LiqPayIntegration, self).__init__(public_key, private_key, host)

        if params is None:
            params = {}
        defaults.update(params)
        # The form fields that will be rendered in the template
        self.fields = {}
        self.fields.update(defaults)

    def add_field(self, key, value):
        self.fields[key] = value

    def add_fields(self, params):
        for (key, val) in params.iteritems():
            self.add_field(key, val)

    def get_urls(self):
        urlpatterns = patterns('',
                               url(r'^notify-handler/$', self.liqpay_notify_handler, name="liqpay_notify_handler"),
                               )
        return urlpatterns

    def res_signature(self, params):
        params = self._prepare_params(params)
        signature_values = [
            self._private_key,
            to_unicode(params.get("amount", u'')),
            to_unicode(params.get("currency", u'')),
            to_unicode(params.get("public_key", u'')),
            to_unicode(params.get("order_id", u'')),
            to_unicode(params.get("type", u'')),
            to_unicode(params.get("description", u'')),
            to_unicode(params.get("status", u'')),
            to_unicode(params.get("transaction_id", u'')),
            to_unicode(params.get("sender_phone", u''))
        ]
        return self._make_signature(*signature_values)

    def get_transaction(self, request):
        logger.info("POST: %s" % request.POST)

        signature = request.POST.get('signature')
        # logger.info("signature: %s" % signature)

        local_signature = self.res_signature(request.POST)
        # logger.info("local_signature: %s" % local_signature)

        result = 'SIGNATURE CHECK ERROR'
        post_data = {}
        trans = None

        if local_signature == signature:
            params = request.POST.copy()
            logger.info("params: %s" % params)
            form = LiqpayBackForm(self, params)
            if not form.is_valid():
                result = ("ERROR %s" % form.errors.as_text()).encode('utf-8')
            else:
                # Apply Changes
                cd = form.cleaned_data
                sum_amount = float(cd['amount'])
                post_data = cd.copy()
                order_id = cd.get('order_id')
                trans = None
                try:
                    trans = TransactionModel.objects.get(order_id=order_id)
                    result = 'DETECTED'
                except TransactionModel.DoesNotExist:
                    trans = TransactionModel.objects.create(
                        version=cd.get('version'),
                        public_key=cd.get('public_key'),
                        amount=sum_amount,
                        currency=cd.get('currency'),
                        description=cd.get('description'),
                        order_id=order_id,
                        pay_type=cd.get('type'),
                        transaction_id=cd.get('transaction_id'),
                        sender_phone=cd.get('sender_phone'),
                        status=cd.get('status'),
                        signature=signature,
                        raw_data=request.POST,
                    )
                    result = 'CREATED'
                except Exception, e:
                    result = e.message.encode('utf-8')
        return post_data, trans, result

    def cnb_form(self):
        return super(LiqPayIntegration, self).cnb_form(self.fields)

    def api(self, url):
        return super(LiqPayIntegration, self).api(url, self.fields)

    def get_signature(self):
        return self.cnb_signature(self.fields)

    @csrf_exempt_m
    @never_cache_m
    @require_POST_m
    def liqpay_notify_handler(self, request):
        post_data, trans, result = self.get_transaction(request)
        if trans:
            if trans.status in self.get_wait_statuses():
                new_status = post_data.get('status')
                if trans.status == new_status:
                    pass
                else:
                    trans.status = new_status
                    if trans.transaction_id == post_data.get('transaction_id'):
                        pass
                    else:
                        trans.transaction_id = post_data.get('transaction_id')
                    trans.save()
            post_data['local_trans_id'] = trans.pk
            post_data['request'] = request
            if trans.status in self.get_valid_statuses():
                order_crypted = post_data.get('order_id')
                order = get_order(order_crypted)[0]
                order.invoice.status = 'invoice_paid'
                order.invoice.save(update_fields=['status'])
                order.invoice.course.status = 'course_paid'
                order.invoice.course.save(update_fields=['status'])
            transaction_was_successful.send(sender=self.__class__,
                                            type="purchase",
                                            response=post_data
                                            )
            result = 'OK'
        return HttpResponse(result)

    @property
    def urls(self):
        return self.get_urls()

    def get_valid_statuses(self, wait_is_valid=False):
        valid_statuses = [
            models.LIQPAY_STATUS_SUCCESS,
            models.LIQPAY_STATUS_SUBSCRIBED,
            models.LIQPAY_STATUS_UNSUBSCRIBED,
            models.LIQPAY_STATUS_REVERSED
        ]
        if wait_is_valid:
            valid_statuses += self.get_wait_statuses()
        if bool(self.fields.get('sandbox')):
            valid_statuses.append(models.LIQPAY_STATUS_SANDBOX)
        return valid_statuses

    def get_wait_statuses(self):
        return [
            models.LIQPAY_STATUS_WAIT_SEQURE,
            models.LIQPAY_STATUS_WAIT_ACCEPT,
            models.LIQPAY_STATUS_WAIT_LC,
            models.LIQPAY_STATUS_PROCESSING
        ]
