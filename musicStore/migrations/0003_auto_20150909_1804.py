# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicStore', '0002_auto_20150909_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='user_rate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
