# Generated by Django 3.2.15 on 2022-10-23 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_feedback_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='percentage',
            new_name='rating',
        ),
    ]
