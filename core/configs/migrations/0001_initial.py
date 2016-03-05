# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, verbose_name='key')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled?')),
                ('value_type', models.CharField(default=b'boolean', max_length=25, verbose_name='type', choices=[(b'boolean', 'Boolean'), (b'date', 'Date'), (b'datetime', 'DateTime'), (b'float', 'Float'), (b'html', 'Html'), (b'html_ml', 'Html multilanguall'), (b'integer', 'Integer'), (b'string', 'String'), (b'string_ml', 'String multilangual'), (b'text', 'Text'), (b'text_ml', 'Text multilanguall')])),
                ('value_name', models.CharField(max_length=255, verbose_name='name')),
                ('value_name_en', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('value_name_ru', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('value_boolean', models.NullBooleanField(verbose_name='value')),
                ('value_integer', models.IntegerField(null=True, verbose_name='value', blank=True)),
                ('value_float', models.FloatField(null=True, verbose_name='value', blank=True)),
                ('value_date', models.DateField(null=True, verbose_name='value', blank=True)),
                ('value_datetime', models.DateTimeField(null=True, verbose_name='value', blank=True)),
                ('value_string', models.CharField(max_length=255, null=True, verbose_name='value', blank=True)),
                ('value_string_ml', models.CharField(max_length=255, null=True, verbose_name='value', blank=True)),
                ('value_string_ml_en', models.CharField(max_length=255, null=True, verbose_name='value', blank=True)),
                ('value_string_ml_ru', models.CharField(max_length=255, null=True, verbose_name='value', blank=True)),
                ('value_text', models.TextField(null=True, verbose_name='value', blank=True)),
                ('value_text_ml', models.TextField(null=True, verbose_name='value', blank=True)),
                ('value_text_ml_en', models.TextField(null=True, verbose_name='value', blank=True)),
                ('value_text_ml_ru', models.TextField(null=True, verbose_name='value', blank=True)),
                ('value_html', tinymce.models.HTMLField(null=True, verbose_name='value', blank=True)),
                ('value_html_ml', tinymce.models.HTMLField(null=True, verbose_name='value', blank=True)),
                ('value_html_ml_en', tinymce.models.HTMLField(null=True, verbose_name='value', blank=True)),
                ('value_html_ml_ru', tinymce.models.HTMLField(null=True, verbose_name='value', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['key'],
                'db_table': 'app_configs',
                'verbose_name': 'app config',
                'verbose_name_plural': 'app configs',
            },
        ),
    ]
