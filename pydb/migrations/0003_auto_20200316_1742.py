# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-16 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pydb', '0002_crews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crews',
            new_name='Crew',
        ),
    ]