# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 04:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qpapers', '0002_auto_20160929_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ques',
            old_name='title',
            new_name='ques',
        ),
    ]