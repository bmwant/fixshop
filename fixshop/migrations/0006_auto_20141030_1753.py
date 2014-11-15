# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixshop', '0005_auto_20141029_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemviews',
            name='session_id',
        ),
        migrations.AddField(
            model_name='itemviews',
            name='session',
            field=models.CharField(max_length=100, verbose_name='user who bought', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='fixshop.Item', verbose_name='items in cart'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cart',
            name='session',
            field=models.CharField(max_length=100, verbose_name='user who bought', null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
