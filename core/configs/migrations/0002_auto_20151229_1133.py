# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfig',
            name='value_decimal',
            field=models.DecimalField(null=True, verbose_name='value', max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='appconfig',
            name='value_link',
            field=models.URLField(null=True, verbose_name='value', blank=True),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='value_type',
            field=models.CharField(default=b'boolean', max_length=25, verbose_name='type', choices=[(b'boolean', 'Boolean'), (b'date', 'Date'), (b'datetime', 'DateTime'), (b'decimal', 'Decimal'), (b'float', 'Float'), (b'html', 'Html'), (b'html_ml', 'Html multilanguall'), (b'integer', 'Integer'), (b'link', 'Link'), (b'string', 'String'), (b'string_ml', 'String multilangual'), (b'text', 'Text'), (b'text_ml', 'Text multilanguall')]),
        ),
    ]
