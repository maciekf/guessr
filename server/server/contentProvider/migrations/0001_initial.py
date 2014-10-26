# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tag', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovieToGuess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('movie', models.FileField(upload_to='movies')),
                ('ending', models.FileField(upload_to='movies')),
                ('guessA', models.CharField(max_length=300)),
                ('guessB', models.CharField(max_length=300)),
                ('hashtags', models.ManyToManyField(to='contentProvider.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
