# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20151217_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intensity',
            name='lessons',
            field=models.DecimalField(default=0, verbose_name='lessons', max_digits=10, decimal_places=0),
        ),
    ]
