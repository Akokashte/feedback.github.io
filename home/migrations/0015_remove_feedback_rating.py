# Generated by Django 3.2.15 on 2023-03-14 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20230315_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='rating',
        ),
    ]