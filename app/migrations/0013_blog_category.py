# Generated by Django 4.0.3 on 2022-06-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('general', 'General'), ('event', 'Event'), ('health', 'Health'), ('tech', 'Technology')], default=None, max_length=50),
        ),
    ]