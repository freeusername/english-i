# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20151228_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duration',
            name='price',
            field=models.DecimalField(null=True, verbose_name='price', max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='duration',
            name='price_en',
            field=models.DecimalField(null=True, verbose_name='price', max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='duration',
            name='price_ru',
            field=models.DecimalField(null=True, verbose_name='price', max_digits=20, decimal_places=2, blank=True),
        ),
    ]
