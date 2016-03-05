# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20151212_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='duration',
            field=models.CharField(default=60, max_length=255, verbose_name='duration', choices=[(60, '60 minutes'), (90, '90 minutes'), (120, '120 minutes')]),
        ),
    ]
