# Generated by Django 4.0.3 on 2022-06-25 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_blog_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
