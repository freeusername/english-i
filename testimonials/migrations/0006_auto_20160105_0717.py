# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0005_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='title',
            field=models.CharField(default=b'', max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='title_en',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='title_ru',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name='title'),
        ),
    ]
