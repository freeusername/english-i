# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_skill_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price_ru',
        ),
        migrations.RemoveField(
            model_name='duration',
            name='full_price_en',
        ),
        migrations.RemoveField(
            model_name='duration',
            name='full_price_ru',
        ),
        migrations.RemoveField(
            model_name='duration',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='duration',
            name='price_ru',
        ),
    ]
