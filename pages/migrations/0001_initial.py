# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', help_text="Example: '/about/'. Make sure to have leading and trailing slashes.", max_length=255, verbose_name='url')),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='title')),
                ('title_en', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('show_title', models.BooleanField(default=True, verbose_name='show title?')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled?')),
                ('content', tinymce.models.HTMLField(default=b'', verbose_name='content', blank=True)),
                ('content_en', tinymce.models.HTMLField(default=b'', null=True, verbose_name='content', blank=True)),
                ('content_ru', tinymce.models.HTMLField(default=b'', null=True, verbose_name='content', blank=True)),
                ('template', models.CharField(default=b'', help_text='Example: about, if not filled will use the default template.', max_length=255, verbose_name='template', blank=True)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
    ]
