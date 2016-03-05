# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20151218_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='skills',
            field=models.ManyToManyField(related_name='personalcourse_skills', verbose_name=b'skills', to='courses.Skill', blank=True),
        ),
    ]
