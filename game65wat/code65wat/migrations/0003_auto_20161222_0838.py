# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code65wat', '0002_auto_20161222_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='id',
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
