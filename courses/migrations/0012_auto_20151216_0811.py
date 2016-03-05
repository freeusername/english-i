# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20151216_0811'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0011_auto_20151214_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalcourse',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='personalcourse',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.AddField(
            model_name='course',
            name='no_skills',
            field=models.BooleanField(default=False, verbose_name='leave it for professionals'),
        ),
        migrations.AddField(
            model_name='course',
            name='skills',
            field=models.ManyToManyField(related_name='personalcourse_skills', null=True, verbose_name=b'skills', to='courses.Skill', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.CharField(default=b'course_front', max_length=255, verbose_name='type', choices=[(b'course_front', 'Course front'), (b'course_personal', 'Course personal')]),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(related_name='personalcourse_user', verbose_name=b'user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.DeleteModel(
            name='PersonalCourse',
        ),
    ]
