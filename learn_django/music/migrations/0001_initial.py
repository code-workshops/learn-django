# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=1000)),
                ('artist', models.CharField(max_length=255)),
            ],
        ),
    ]
