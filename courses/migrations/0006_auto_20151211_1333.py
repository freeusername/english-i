# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_auto_20151210_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='position')),
                ('no_skills', models.BooleanField(default=False, verbose_name='leave it for professionals')),
                ('price', models.DecimalField(null=True, verbose_name='price', max_digits=20, decimal_places=2, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'personal course',
                'verbose_name_plural': 'personal courses',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='position')),
                ('recommended', models.BooleanField(default=False, verbose_name='recommended?')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('lessons', models.PositiveSmallIntegerField(default=0, verbose_name='lessons')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='duration')),
                ('lesson_price', models.DecimalField(null=True, verbose_name='price per lesson', max_digits=20, decimal_places=2, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='position')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_en', models.TextField(null=True, verbose_name='description', blank=True)),
                ('description_ru', models.TextField(null=True, verbose_name='description', blank=True)),
                ('lessons', models.PositiveSmallIntegerField(default=0, verbose_name='lessons')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.RenameField(
            model_name='course',
            old_name='length',
            new_name='duration',
        ),
        migrations.AddField(
            model_name='personalcourse',
            name='skills',
            field=models.ManyToManyField(related_name='personalcourse_skills', verbose_name=b'skills', to='courses.Skill'),
        ),
        migrations.AddField(
            model_name='personalcourse',
            name='user',
            field=models.ForeignKey(related_name='personalcourse_user', verbose_name=b'user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='skill',
            field=models.ForeignKey(related_name='course_skill', verbose_name=b'skill', blank=True, to='courses.Skill', null=True),
        ),
    ]
