# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20151228_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skype',
            field=models.CharField(max_length=255, null=True, verbose_name='skype name', blank=True),
        ),
    ]
