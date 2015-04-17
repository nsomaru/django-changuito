# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django_fsm
import changuito.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('changuito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=64)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('payment_proof', changuito.fields.RestrictedFileField(null=True, upload_to=b'payment', blank=True)),
                ('shipping_address', models.TextField()),
                ('customer_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=75)),
                ('uuid', django_extensions.db.fields.ShortUUIDField(editable=False, blank=True)),
                ('state', django_fsm.FSMField(default=b'open', protected=True, max_length=50)),
                ('cart', models.OneToOneField(to='changuito.Cart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(verbose_name='quantity', max_digits=18, decimal_places=3),
            preserve_default=True,
        ),
    ]
