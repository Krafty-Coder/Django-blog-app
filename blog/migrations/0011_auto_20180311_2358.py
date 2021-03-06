# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-11 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180311_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
