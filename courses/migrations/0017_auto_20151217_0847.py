# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20151217_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duration',
            options={'ordering': ('duration',), 'verbose_name': 'duration', 'verbose_name_plural': 'durations'},
        ),
    ]
