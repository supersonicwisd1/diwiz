# Generated by Django 4.0.3 on 2022-07-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_blog_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='info',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='home',
            name='info',
            field=models.CharField(max_length=1000),
        ),
    ]
