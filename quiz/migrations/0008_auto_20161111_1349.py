# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20161108_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Quiz End Date (UTC)'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Quiz Start Date (UTC)'),
        ),
    ]
