# Generated by Django 3.2.15 on 2023-02-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_percentage_feedback_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('branch', models.CharField(default='', max_length=150)),
                ('myclass', models.CharField(default='', max_length=150)),
                ('sem', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
