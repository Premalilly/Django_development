# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-02 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devApp', '0005_auto_20180502_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicemodel',
            name='date',
        ),
    ]