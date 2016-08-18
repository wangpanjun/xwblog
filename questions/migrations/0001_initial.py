# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('answer_id', models.AutoField(serialize=False, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('answer', models.TextField(null=True)),
                ('detail', models.TextField(null=True)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('question_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=512, null=True, db_index=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('answers', models.ManyToManyField(to='questions.AnswerModel', blank=True)),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=62)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='tags',
            field=models.ManyToManyField(to='questions.TagModel', blank=True),
        ),
    ]
