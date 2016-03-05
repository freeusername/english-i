# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20151208_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='length',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='course duration', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='number of lessons', blank=True),
        ),
    ]
