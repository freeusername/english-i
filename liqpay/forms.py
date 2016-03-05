# coding: UTF-8
from django import forms

from . import models

class LiqpayBackForm(forms.Form):

    def __init__(self, integration, *args, **kwargs):
        self.integration = integration
        super(LiqpayBackForm, self).__init__(*args, **kwargs)

    version = forms.CharField()
    public_key = forms.CharField()
    amount = forms.DecimalField()
    currency = forms.ChoiceField(choices=models.LIQPAY_CCY_CHOICES)
    description = forms.CharField()
    order_id = forms.CharField()
    status = forms.CharField()
    type = forms.CharField(required=False)
    transaction_id = forms.CharField(required=False)
    sender_phone = forms.CharField(required=False)

