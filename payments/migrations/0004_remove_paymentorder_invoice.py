# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20151220_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentorder',
            name='invoice',
        ),
    ]
