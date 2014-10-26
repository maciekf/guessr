# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentProvider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movietoguess',
            name='ending',
        ),
        migrations.AddField(
            model_name='movietoguess',
            name='guessSecond',
            field=models.CharField(max_length=20, default='zzz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movietoguess',
            name='minature',
            field=models.FileField(upload_to='minatures', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movietoguess',
            name='question',
            field=models.CharField(max_length=300, default='What will happen next?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movietoguess',
            name='movie',
            field=models.FileField(upload_to='movies', null=True),
            preserve_default=True,
        ),
    ]
