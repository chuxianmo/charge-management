# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20170921_2048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSuggestions',
            new_name='Suggestions',
        ),
    ]
