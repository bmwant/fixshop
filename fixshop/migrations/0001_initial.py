# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkouted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('picture', models.FileField(upload_to='')),
                ('desc', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('item_id', models.ForeignKey(verbose_name='what item', to='fixshop.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='itemviews',
            name='session_id',
            field=models.ForeignKey(verbose_name='who views', to='fixshop.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(verbose_name='items in cart', to='fixshop.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(verbose_name='user who bought', to='fixshop.Session'),
            preserve_default=True,
        ),
    ]
