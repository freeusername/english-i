# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20151228_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='show',
            field=models.BooleanField(default=False, verbose_name='show link?'),
        ),
    ]
