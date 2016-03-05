# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151207_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='avatar', blank=True),
        ),
    ]
