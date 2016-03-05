# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='description',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='link',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='small_description_en',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='small_description_ru',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='title_ru',
        ),
        migrations.AddField(
            model_name='slide',
            name='bottom_text',
            field=models.TextField(null=True, verbose_name='bottom text', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='bottom_text_en',
            field=models.TextField(null=True, verbose_name='bottom text', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='bottom_text_ru',
            field=models.TextField(null=True, verbose_name='bottom text', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='top_text',
            field=models.TextField(null=True, verbose_name='top text', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='top_text_en',
            field=models.TextField(null=True, verbose_name='top text', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='top_text_ru',
            field=models.TextField(null=True, verbose_name='top text', blank=True),
        ),
    ]
