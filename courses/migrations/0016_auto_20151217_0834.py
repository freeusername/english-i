# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20151216_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duration',
            name='duration',
            field=models.DecimalField(default=60, verbose_name='duration', max_digits=10, decimal_places=0),
        ),
    ]
