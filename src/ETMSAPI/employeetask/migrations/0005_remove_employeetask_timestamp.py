# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-29 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeetask', '0004_auto_20191129_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeetask',
            name='timestamp',
        ),
    ]
