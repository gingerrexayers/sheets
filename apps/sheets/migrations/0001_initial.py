# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.10.1 on 2016-09-29 22:16
=======
# Generated by Django 1.10.1 on 2016-09-29 23:58
>>>>>>> bde9fab659be23b533e3ce8e25fc2cc5fc929d69
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0004_remove_user_date_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alignment', models.CharField(max_length=255)),
                ('race', models.CharField(max_length=255)),
                ('char_class', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=1)),
                ('exp', models.IntegerField(default=0)),
                ('curr_hp', models.IntegerField()),
                ('max_hp', models.IntegerField()),
                ('damage', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
    ]
