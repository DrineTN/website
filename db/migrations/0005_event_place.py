# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20160205_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default='FSS', max_length=80),
        ),
    ]