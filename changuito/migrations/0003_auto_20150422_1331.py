# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changuito', '0002_auto_20150417_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='uuid',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='000000000', max_length=32),
            preserve_default=False,
        ),
    ]
