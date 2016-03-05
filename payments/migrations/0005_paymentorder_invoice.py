# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20151228_1906'),
        ('payments', '0004_remove_paymentorder_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentorder',
            name='invoice',
            field=models.ForeignKey(related_name='payment_orders', verbose_name='invoice', blank=True, to='invoices.Invoice', null=True),
        ),
    ]
