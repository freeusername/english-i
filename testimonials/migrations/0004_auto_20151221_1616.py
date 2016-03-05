# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_auto_20151214_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='location',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='location_en',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='location_ru',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='info',
            field=models.CharField(max_length=255, null=True, verbose_name='info', blank=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='info_en',
            field=models.CharField(max_length=255, null=True, verbose_name='info', blank=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='info_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='info', blank=True),
        ),
    ]
