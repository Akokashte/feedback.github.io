# Generated by Django 3.2.15 on 2022-09-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=50)),
                ('q2', models.CharField(max_length=50)),
                ('q3', models.CharField(max_length=50)),
                ('q4', models.CharField(max_length=50)),
                ('q5', models.CharField(max_length=50)),
                ('q6', models.CharField(max_length=50)),
                ('q7', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
