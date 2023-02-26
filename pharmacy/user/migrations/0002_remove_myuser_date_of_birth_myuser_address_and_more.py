# Generated by Django 4.0.6 on 2023-02-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
