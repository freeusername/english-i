# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20151207_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='course',
            name='preview',
            field=models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='preview'),
        ),
    ]
