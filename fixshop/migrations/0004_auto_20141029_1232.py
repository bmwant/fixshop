# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixshop', '0003_auto_20141029_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='picture',
        ),
    ]
