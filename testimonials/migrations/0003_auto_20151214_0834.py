# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
    ]
