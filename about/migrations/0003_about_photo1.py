# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20161013_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='photo1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
