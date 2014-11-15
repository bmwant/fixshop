# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='picture',
            new_name='image',
        ),
    ]
