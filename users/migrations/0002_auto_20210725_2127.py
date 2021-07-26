# Generated by Django 3.1 on 2021-07-25 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0003_auto_20210725_1215'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighourhood',
        ),
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.neighborhood'),
        ),
    ]