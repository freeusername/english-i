# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20151214_0855'),
        ('accounts', '0003_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPersonalCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default='course_notpaid', max_length=255, verbose_name='status', choices=[('course_notpaid', 'not paid'), ('course_paid', 'paid'), ('course_started', 'started'), ('course_finished', 'finished')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('course', models.ForeignKey(related_name='courses_personalcourse', verbose_name='personal course', to='courses.PersonalCourse')),
                ('user', models.ForeignKey(related_name='users_personalcourse', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user course',
                'verbose_name_plural': 'user courses',
            },
        ),
        migrations.AddField(
            model_name='usercourse',
            name='status',
            field=models.CharField(default='course_notpaid', max_length=255, verbose_name='status', choices=[('course_notpaid', 'not paid'), ('course_paid', 'paid'), ('course_started', 'started'), ('course_finished', 'finished')]),
        ),
    ]
