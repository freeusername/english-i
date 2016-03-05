# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151228_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='duration',
            field=models.ForeignKey(related_name='courses_course', verbose_name='duration', blank=True, to='courses.Duration', null=True),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='intensity',
            field=models.ForeignKey(related_name='courses_course', verbose_name='intensity', blank=True, to='courses.Intensity', null=True),
        ),
    ]
