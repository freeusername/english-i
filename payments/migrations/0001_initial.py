# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=32, verbose_name='version')),
                ('public_key', models.CharField(max_length=32, verbose_name='public key')),
                ('amount', models.DecimalField(verbose_name='amount', max_digits=16, decimal_places=2)),
                ('currency', models.CharField(max_length=32, verbose_name='currency')),
                ('description', models.CharField(max_length=128, verbose_name='description')),
                ('order_id', models.CharField(max_length=255, verbose_name='order id')),
                ('pay_type', models.CharField(default=b'buy', max_length=32, verbose_name='payment type', blank=True)),
                ('transaction_id', models.CharField(max_length=128, null=True, verbose_name='transaction id', blank=True)),
                ('sender_phone', models.CharField(max_length=32, null=True, verbose_name='sender phone', blank=True)),
                ('status', models.CharField(max_length=32, verbose_name='status')),
                ('signature', models.TextField(verbose_name='signature')),
                ('raw_data', models.TextField(null=True, verbose_name='raw data', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
            },
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.PositiveIntegerField(null=True, blank=True)),
                ('sum', models.DecimalField(default=0, verbose_name='sum', max_digits=16, decimal_places=2)),
                ('date_begin', models.DateField(null=True, verbose_name='date begin')),
                ('date_end', models.DateField(null=True, verbose_name='date end')),
                ('backend', models.CharField(default=b'admin', max_length=32, verbose_name=b'bakend', choices=[(b'admin', b'Admin'), (b'liqpay', b'LiqPay')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('transaction_type', models.ForeignKey(related_name='payment_orders', blank=True, to='contenttypes.ContentType', null=True)),
                ('user', models.ForeignKey(related_name='payment_orders', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'payment order',
                'verbose_name_plural': 'payment orders',
            },
        ),
    ]
