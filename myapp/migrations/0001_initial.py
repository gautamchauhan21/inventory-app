# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('inventory_name', models.CharField(help_text='This contains the Inventory name:', max_length=200, verbose_name='INVENTORY NAME')),
                ('short_name', models.CharField(help_text='This contains an abbreviation:', max_length=20)),
                ('inventory_code', models.IntegerField(default='0', help_text='This contains the Inventory code:', verbose_name='INVENTORY CODE')),
                ('price', models.IntegerField(default='0')),
                ('stocks_left', models.IntegerField(default='0', verbose_name='STOCKS LEFT')),
            ],
        ),
    ]
