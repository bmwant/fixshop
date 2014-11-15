# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixshop', '0004_auto_20141029_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(null=True, to='fixshop.Item', verbose_name='items in cart'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(null=True, to='fixshop.Session', verbose_name='user who bought'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.FileField(upload_to='items'),
            preserve_default=True,
        ),
    ]
