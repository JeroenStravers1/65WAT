# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('code65wat', '0005_auto_20161222_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='attack_countdown',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 21, 12, 4, 315066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 21, 12, 4, 315066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='upgrade_countdown',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 22, 21, 12, 4, 315066, tzinfo=utc)),
        ),
    ]
