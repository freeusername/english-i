# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20151216_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'invoice_notpaid', max_length=255, verbose_name='status', choices=[(b'invoice_notpaid', 'Not paid'), (b'invoice_paid', 'Paid')])),
                ('price', models.DecimalField(default=0, verbose_name='price', max_digits=20, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('course', models.ForeignKey(related_name='invoice_course', verbose_name=b'course', to='accounts.UserCourse')),
                ('user', models.ForeignKey(related_name='invoice_user', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'invoice',
                'verbose_name_plural': 'invoices',
            },
        ),
    ]
