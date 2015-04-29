# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changuito', '0003_auto_20150422_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
