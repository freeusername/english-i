# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20151219_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='price_en',
            field=models.DecimalField(default=0, null=True, verbose_name='price', max_digits=20, decimal_places=2),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_ru',
            field=models.DecimalField(default=0, null=True, verbose_name='price', max_digits=20, decimal_places=2),
        ),
    ]
