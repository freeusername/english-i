# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='length',
            field=models.DecimalField(default=0, verbose_name='course duration', max_digits=20, decimal_places=0, blank=True),
        ),
    ]
