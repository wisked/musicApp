# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='user_rate',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='album_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='album',
            field=models.ForeignKey(to='musicStore.Album'),
        ),
    ]
