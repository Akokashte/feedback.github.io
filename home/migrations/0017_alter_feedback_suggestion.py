# Generated by Django 3.2.15 on 2023-03-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20230315_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='suggestion',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
