# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_paymentorder_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentorder',
            name='date_begin',
        ),
        migrations.RemoveField(
            model_name='paymentorder',
            name='date_end',
        ),
    ]
