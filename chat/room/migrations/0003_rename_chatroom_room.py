# Generated by Django 4.1.2 on 2022-12-07 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatRoom',
            new_name='Room',
        ),
    ]
