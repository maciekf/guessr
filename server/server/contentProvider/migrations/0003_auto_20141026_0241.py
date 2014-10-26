# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentProvider', '0002_auto_20141026_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movietoguess',
            old_name='guessA',
            new_name='goodAnswer',
        ),
        migrations.RenameField(
            model_name='movietoguess',
            old_name='guessSecond',
            new_name='stopTime',
        ),
        migrations.RenameField(
            model_name='movietoguess',
            old_name='guessB',
            new_name='wrongAnswer',
        ),
    ]
