# Generated by Django 5.0.4 on 2024-04-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='mba',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mca',
        ),
    ]