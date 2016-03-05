# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255, verbose_name='URL-path', blank=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('keywords', models.CharField(max_length=255, verbose_name='keywords', blank=True)),
                ('keywords_en', models.CharField(max_length=255, null=True, verbose_name='keywords', blank=True)),
                ('keywords_ru', models.CharField(max_length=255, null=True, verbose_name='keywords', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('description_en', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_ru', models.TextField(null=True, verbose_name='description', blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'meta_tags',
                'verbose_name': 'meta tags',
                'verbose_name_plural': 'meta tags',
            },
        ),
        migrations.AlterUniqueTogether(
            name='metatag',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
