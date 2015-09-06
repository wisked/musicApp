# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('describe', models.TextField(blank=True, verbose_name='album description')),
                ('release_date', models.DateField()),
                ('image', models.ImageField(upload_to='images/%Y')),
                ('album_rate', models.IntegerField(default=0)),
                ('date_add', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='artist name', max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('beginning', models.DateField(verbose_name='carier start')),
                ('end', models.CharField(verbose_name='carier end', max_length=50)),
                ('biography', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photo/%Y')),
                ('artist_rate', models.IntegerField(default=0)),
                ('date_create', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='musicStore.Artist'),
        ),
    ]
