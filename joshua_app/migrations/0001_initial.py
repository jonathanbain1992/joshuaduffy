# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_finish', models.DateField()),
                ('grade', models.CharField(max_length=100)),
                ('description_comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('institution_address', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('year_start', models.DateField()),
                ('year_finish', models.DateField()),
                ('classification', models.CharField(default=None, max_length=100, verbose_name=((0, 'First Class'), (1, 'Upper Second Class'), (2, 'Lower Second Class'), (3, 'Third Class'), (4, 'Ordinary Degree'), (5, 'Did Not Complete')))),
                ('referee_name', models.CharField(max_length=100)),
                ('refee_contact', models.CharField(max_length=100)),
                ('comments', models.TextField()),
                ('class_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='joshua_app.Class_Item')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_category', models.CharField(choices=[(0, 'Self Employment'), (1, 'Professional Employment'), (2, 'Casual Employment'), (3, 'Charity'), (4, 'Primary Education'), (5, 'Secondary Education'), (6, 'Further Education'), (7, 'Higher Education (Undergraduate)'), (8, 'Higher Education (Postgraduate)')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('sur_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('personal_statement', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joshua_app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('institution_address', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('year_start', models.DateField()),
                ('year_finish', models.DateField()),
                ('role_desc', models.TextField()),
                ('referee_name', models.CharField(max_length=100)),
                ('refee_contact', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joshua_app.Work_Item'),
        ),
    ]
