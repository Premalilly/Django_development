# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-02 05:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date'),
        ),
    ]
