# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, verbose_name='show?')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='title')),
                ('title_en', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('description', models.TextField(default=b'', verbose_name='description')),
                ('description_en', models.TextField(default=b'', null=True, verbose_name='description')),
                ('description_ru', models.TextField(default=b'', null=True, verbose_name='description')),
                ('full_name', models.CharField(max_length=255, null=True, verbose_name='full name', blank=True)),
                ('full_name_en', models.CharField(max_length=255, null=True, verbose_name='full name', blank=True)),
                ('full_name_ru', models.CharField(max_length=255, null=True, verbose_name='full name', blank=True)),
                ('location', models.CharField(max_length=255, null=True, verbose_name='location', blank=True)),
                ('location_en', models.CharField(max_length=255, null=True, verbose_name='location', blank=True)),
                ('location_ru', models.CharField(max_length=255, null=True, verbose_name='location', blank=True)),
                ('image', models.ImageField(upload_to=core.utils.helpers.get_file_path, null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'testimonial',
                'verbose_name_plural': 'testimonials',
            },
        ),
    ]
