# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(default=b'invoice_notpaid', verbose_name='status', max_length=255, editable=False, choices=[(b'invoice_notpaid', 'Not paid'), (b'invoice_paid', 'Paid')]),
        ),
    ]
