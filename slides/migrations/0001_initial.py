# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, verbose_name='show?')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_en', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_ru', models.TextField(null=True, verbose_name='description', blank=True)),
                ('small_description', models.TextField(null=True, verbose_name='small_description', blank=True)),
                ('small_description_en', models.TextField(null=True, verbose_name='small_description', blank=True)),
                ('small_description_ru', models.TextField(null=True, verbose_name='small_description', blank=True)),
                ('link', models.URLField(null=True, verbose_name='link', blank=True)),
                ('image', models.ImageField(upload_to=core.utils.helpers.get_file_path, verbose_name='slide')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'slide',
                'verbose_name_plural': 'slides',
            },
        ),
    ]
