# Generated by Django 3.2.15 on 2023-02-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_academicform'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicform',
            name='sem',
            field=models.CharField(default='', max_length=50),
        ),
    ]