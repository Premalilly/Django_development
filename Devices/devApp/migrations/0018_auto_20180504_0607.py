# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devApp', '0017_auto_20180503_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemodel',
            name='payment_expiry',
            field=models.FloatField(default=False),
        ),
    ]
