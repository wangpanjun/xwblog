# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField(blank=True)),
                ('views', models.IntegerField(default=0)),
                ('images', models.CharField(max_length=256, blank=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='category',
            field=models.ForeignKey(to='articles.CategoryModel'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='tags',
            field=models.ManyToManyField(to='questions.TagModel'),
        ),
    ]
