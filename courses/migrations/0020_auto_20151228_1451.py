# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20151219_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='duration',
            name='full_price_en',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, blank=True, null=True, verbose_name='full price'),
        ),
        migrations.AddField(
            model_name='duration',
            name='full_price_ru',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, blank=True, null=True, verbose_name='full price'),
        ),
        migrations.AddField(
            model_name='duration',
            name='price_en',
            field=models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='Price for 60 minutes.', null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='duration',
            name='price_ru',
            field=models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='Price for 60 minutes.', null=True, verbose_name='price'),
        ),
    ]
