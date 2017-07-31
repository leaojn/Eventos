# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tags',
            field=models.ManyToManyField(related_name='tags_do_usuario', through='core.Tag_Usuario', to='core.Tag'),
        ),
    ]