# Generated by Django 5.1.2 on 2024-12-16 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_no',
        ),
    ]
