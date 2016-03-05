# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20151213_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.PositiveIntegerField(default=60, verbose_name='duration')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, blank=True, help_text='Price for 60 minutes.', null=True, verbose_name='price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'duration',
                'verbose_name_plural': 'durations',
            },
        ),
        migrations.CreateModel(
            name='Intensity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='position')),
                ('recommended', models.BooleanField(default=False, verbose_name='recommended?')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('lessons', models.PositiveSmallIntegerField(default=0, verbose_name='lessons')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'intensity',
                'verbose_name_plural': 'intensities',
            },
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='duration',
            name='intensity',
            field=models.ForeignKey(related_name='duration_intensity', verbose_name=b'intensity', to='courses.Intensity'),
        ),
    ]
