# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20151228_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price_ru',
        ),
    ]
