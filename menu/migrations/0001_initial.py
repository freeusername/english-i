# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='name')),
                ('title_en', models.CharField(default=b'', max_length=255, null=True, verbose_name='name')),
                ('title_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name='name')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('link', models.CharField(default=b'', help_text='example: /about/', max_length=255, verbose_name='url', blank=True)),
                ('search_template', models.CharField(default=b'^{}', max_length=255, verbose_name='search template', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
    ]
