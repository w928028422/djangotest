# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20170603_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]
