# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20151216_1525'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentorder',
            name='invoice',
            field=models.ForeignKey(related_name='payment_order', verbose_name='invoice', blank=True, to='invoices.Invoice', null=True),
        ),
    ]
