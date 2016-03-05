# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20151214_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='preview', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pros_cons',
            field=models.TextField(null=True, verbose_name='pros and cons of the course', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pros_cons_en',
            field=models.TextField(null=True, verbose_name='pros and cons of the course', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pros_cons_ru',
            field=models.TextField(null=True, verbose_name='pros and cons of the course', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(null=True, verbose_name='short description', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='short description', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='short description', blank=True),
        ),
    ]
