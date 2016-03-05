# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveIntegerField(default=0, verbose_name='position')),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='title')),
                ('title_en', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name='title')),
                ('short_description', models.TextField(default=b'', verbose_name='short description')),
                ('short_description_en', models.TextField(default=b'', null=True, verbose_name='short description')),
                ('short_description_ru', models.TextField(default=b'', null=True, verbose_name='short description')),
                ('description', models.TextField(default=b'', verbose_name='description')),
                ('description_en', models.TextField(default=b'', null=True, verbose_name='description')),
                ('description_ru', models.TextField(default=b'', null=True, verbose_name='description')),
                ('lessons', models.DecimalField(default=0, verbose_name='number of lessons', max_digits=20, decimal_places=0, blank=True)),
                ('length', models.DecimalField(default=0, verbose_name='course length', max_digits=20, decimal_places=0, blank=True)),
                ('pros_cons', models.TextField(default=b'', verbose_name='pros and cons of the course')),
                ('pros_cons_en', models.TextField(default=b'', null=True, verbose_name='pros and cons of the course')),
                ('pros_cons_ru', models.TextField(default=b'', null=True, verbose_name='pros and cons of the course')),
                ('price', models.DecimalField(default=0, verbose_name='price', max_digits=20, decimal_places=2, blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
    ]
