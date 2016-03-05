# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20151216_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='duration',
            name='full_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=20, blank=True, null=True, verbose_name='price'),
        ),
    ]
