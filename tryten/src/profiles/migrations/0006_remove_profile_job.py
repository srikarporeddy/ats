# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-26 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170526_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
    ]
