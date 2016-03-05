# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20151214_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='intensity',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='intensity',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
    ]
