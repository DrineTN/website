# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_official',
            field=models.BooleanField(default=False),
        ),
    ]
