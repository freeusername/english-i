# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20151228_1906'),
        ('accounts', '0006_remove_user_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='duration',
            field=models.ForeignKey(related_name='courses_course', verbose_name='course', blank=True, to='courses.Duration', null=True),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='intensity',
            field=models.ForeignKey(related_name='courses_course', verbose_name='course', blank=True, to='courses.Intensity', null=True),
        ),
    ]
