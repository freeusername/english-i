# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20151216_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='type',
            new_name='value_type',
        ),
    ]
