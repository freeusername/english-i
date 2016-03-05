# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0004_auto_20151221_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, verbose_name='show?')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('full_name', models.CharField(default=b'', max_length=255, verbose_name='full name')),
                ('full_name_en', models.CharField(default=b'', max_length=255, null=True, verbose_name='full name')),
                ('full_name_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name='full name')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_en', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_ru', models.TextField(null=True, verbose_name='description', blank=True)),
                ('image', models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
        ),
    ]
