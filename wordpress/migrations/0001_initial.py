# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(help_text='The site ID on Wordpress.com')),
                ('wp_id', models.IntegerField(help_text='The object ID on Wordpress.com')),
                ('login', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('nice_name', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('avatar_url', models.CharField(max_length=1000)),
                ('profile_url', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(help_text='The site ID on Wordpress.com')),
                ('wp_id', models.IntegerField(help_text='The object ID on Wordpress.com')),
                ('name', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
                ('description', models.TextField(blank=True)),
                ('post_count', models.IntegerField()),
                ('parent_wp_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(help_text='The site ID on Wordpress.com')),
                ('wp_id', models.IntegerField(help_text='The object ID on Wordpress.com')),
                ('url', models.CharField(help_text='The full URL to the media file', max_length=1000)),
                ('guid', models.CharField(blank=True, db_index=True, max_length=1000, null=True)),
                ('uploaded_date', models.DateTimeField()),
                ('post_ID', models.IntegerField(blank=True, help_text='ID of the post this media is attached to', null=True)),
                ('file_name', models.CharField(blank=True, max_length=500, null=True)),
                ('file_extension', models.CharField(blank=True, max_length=10, null=True)),
                ('mime_type', models.CharField(blank=True, max_length=200, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('caption', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('alt', models.TextField(blank=True, null=True)),
                ('exif', jsonfield.fields.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(help_text='The site ID on Wordpress.com')),
                ('wp_id', models.IntegerField(help_text='The object ID on Wordpress.com')),
                ('post_date', models.DateTimeField()),
                ('modified', models.DateTimeField(help_text="The post's most recent update time")),
                ('title', models.TextField(blank=True, null=True)),
                ('url', models.CharField(help_text='The full permalink URL to the post', max_length=1000)),
                ('short_url', models.CharField(help_text='The wp.me short URL', max_length=1000)),
                ('content', models.TextField(blank=True, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('guid', models.CharField(blank=True, db_index=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('sticky', models.BooleanField(default=False, help_text='Show this post at the top of the chronological list, even if old.')),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
                ('parent', jsonfield.fields.JSONField(blank=True, null=True)),
                ('post_type', models.CharField(blank=True, max_length=20, null=True)),
                ('likes_enabled', models.NullBooleanField()),
                ('sharing_enabled', models.NullBooleanField()),
                ('like_count', models.IntegerField(blank=True, null=True)),
                ('global_ID', models.CharField(max_length=1000)),
                ('featured_image', models.CharField(max_length=1000)),
                ('post_thumbnail', jsonfield.fields.JSONField(blank=True, null=True)),
                ('format', models.CharField(max_length=20)),
                ('menu_order', models.IntegerField(blank=True, null=True)),
                ('metadata', jsonfield.fields.JSONField()),
                ('attachments', models.ManyToManyField(blank=True, to='wordpress.Media')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wordpress.Author')),
                ('categories', models.ManyToManyField(blank=True, to='wordpress.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(help_text='The site ID on Wordpress.com')),
                ('wp_id', models.IntegerField(help_text='The object ID on Wordpress.com')),
                ('name', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
                ('description', models.TextField(blank=True)),
                ('post_count', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('wp_id', 'site_id')]),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='wordpress.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='media',
            unique_together=set([('wp_id', 'site_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('wp_id', 'site_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('wp_id', 'site_id')]),
        ),
    ]
