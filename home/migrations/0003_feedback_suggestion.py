# Generated by Django 3.2.15 on 2022-09-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220910_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='suggestion',
            field=models.CharField(default='', max_length=150),
        ),
    ]
