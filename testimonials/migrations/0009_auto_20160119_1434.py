# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0008_auto_20160105_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='title',
            field=models.CharField(default=b'', max_length=27, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='title_en',
            field=models.CharField(default=b'', max_length=27, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='title_ru',
            field=models.CharField(default=b'', max_length=27, null=True, verbose_name='title'),
        ),
    ]
