# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('order', models.PositiveIntegerField(default=2, verbose_name='Order')),
                ('span', models.PositiveIntegerField(default=10, verbose_name='Timespan (in seconds)')),
            ],
        ),
    ]
