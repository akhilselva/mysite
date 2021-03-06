# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=25)),
                ('book_name', models.CharField(default='', max_length=140)),
            ],
        ),
        migrations.RemoveField(
            model_name='buy',
            name='title',
        ),
        migrations.AddField(
            model_name='buy',
            name='author',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='buy',
            name='book_image',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='buy',
            name='book_title',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='buy',
            name='publisher',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='books',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.buy'),
        ),
    ]
