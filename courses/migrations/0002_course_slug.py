# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=255, blank=True, help_text='If you do not specify this field, it will be generated <b>automatically</b>.', unique=True, verbose_name='URL-path'),
        ),
    ]
