# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import changuito.models
import changuito.fields


class Migration(migrations.Migration):

    dependencies = [
        ('changuito', '0004_order_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_proof',
            field=changuito.fields.RestrictedFileField(null=True, upload_to=changuito.models.upload_path, blank=True),
            preserve_default=True,
        ),
    ]
