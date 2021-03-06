# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


def migrate_date(apps, schema_editor):
    Event = apps.get_model('db', 'Event')
    rows = Event.objects.all()
    for row in rows:
        if row.start_date:
            row.start = django.utils.timezone.make_aware(
                django.utils.timezone.datetime(
                    row.start_date.year,
                    row.start_date.month,
                    row.start_date.day))
        if row.end_date:
            row.end = django.utils.timezone.make_aware(
                django.utils.timezone.datetime(
                    row.end_date.year,
                    row.end_date.month,
                    row.end_date.day))
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0023_auto_20161108_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_date),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[('con', 'conference'), ('cha', 'challenge'), ('tra', 'training'), ('tlk', 'talk')], max_length=3),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(default='Faculty of Sciences of Sfax, Amphi A9', max_length=80),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='education',
            field=models.CharField(blank=True, choices=[('LF', 'Licence Fondamentale'), ('LA', 'Licence Appliqué'), ('P', 'Préparatoire'), ('ENG', 'Ingéniorat'),
                                                        ('MR', 'Master de Recherche'), ('MP', 'Master Professionnel'), ('PHD', 'Doctorat')], max_length=3, verbose_name='Diplome courant'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='university',
            field=models.CharField(blank=True, choices=[('FSS', 'Faculté des Sciences de Sfax'), ('ENIS', 'Ecole Nationale des Ingénieurs de Sfax'), ('ISIMS', "Institut Supérieur d'Informatique et de Multimédia de Sfax"), ('ENETCOM', "Ecole Nationale d'electronique et de télécommunications de Sfax"), ('FSEGS', 'Faculté des Sciences Economiques et de Gestion de Sfax'), (
                'IPEIS', "Institut Préparatoire aux Etudes d'Ingénieurs de Sfax"), ('ISGIS', 'Institut Supérieur de Gestion Industrielle de Sfax'), ('IPSAS', 'Institut Polytechnique Privé des Sciences Avancées de Sfax'), ('ISETS', 'Institut Supérieur des Etudes Technologiques de Sfax'), ('IIT', 'Institut International de Technologie Sfax')], max_length=7, verbose_name='Institution / University'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='year',
            field=models.CharField(blank=True, choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1, verbose_name='Année'),
        ),
    ]
