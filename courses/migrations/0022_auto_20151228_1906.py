# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20151228_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price_en',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, blank=True, null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='course',
            name='price_ru',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, blank=True, null=True, verbose_name='price'),
        ),
    ]
