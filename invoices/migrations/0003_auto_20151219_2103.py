# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20151216_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(default=b'invoice_noprice', verbose_name='status', max_length=255, editable=False, choices=[(b'invoice_noprice', 'No price'), (b'invoice_notpaid', 'Not paid'), (b'invoice_paid', 'Paid')]),
        ),
    ]
