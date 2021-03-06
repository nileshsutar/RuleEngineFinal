# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 10:30
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import ruleengine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rulename', models.CharField(max_length=30, unique=True, verbose_name='rulename')),
                ('datafile', models.FileField(max_length=10000, upload_to=ruleengine.models.user_directory_path)),
                ('filelocation', models.CharField(max_length=255, verbose_name='filelocation')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hours', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('minutes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('schedulertype', models.CharField(max_length=20, verbose_name='schedulertype')),
            ],
            options={
                'db_table': 'rules',
            },
        ),
        migrations.CreateModel(
            name='RuleExecutionSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rulename', models.CharField(max_length=30, verbose_name='rulename')),
                ('ruleid', models.PositiveIntegerField(verbose_name='ruleid')),
                ('starttime', models.DateTimeField(default=datetime.datetime.now, verbose_name='starttime')),
                ('stoptime', models.DateTimeField(default=datetime.datetime.now, verbose_name='stoptime')),
                ('status', models.CharField(max_length=20, verbose_name='status')),
                ('filelocation', models.CharField(max_length=255, verbose_name='filelocation')),
                ('error_message', models.CharField(max_length=255, verbose_name='error_message')),
            ],
            options={
                'db_table': 'ruleexecutionsummary',
            },
        ),
    ]
