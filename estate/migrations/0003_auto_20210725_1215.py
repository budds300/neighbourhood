# Generated by Django 3.1 on 2021-07-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('estate', '0002_auto_20210725_1154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Neighbourhood',
            new_name='Neighborhood',
        ),
    ]