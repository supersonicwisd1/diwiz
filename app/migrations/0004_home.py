# Generated by Django 4.0.3 on 2022-06-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
