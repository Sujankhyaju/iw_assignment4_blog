# Generated by Django 3.0.3 on 2020-07-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='photo',
        ),
    ]
