# Generated by Django 3.0.4 on 2021-04-18 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.URLField(default='https://via.placeholder.com/300x400?text=No+photo', max_length=900)),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('notes', models.TextField(default='', max_length=200)),
            ],
        ),
    ]
