# Generated by Django 4.2 on 2023-04-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_newfeedback_s2_q1_newfeedback_s2_q2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_q7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_subject_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_suggestion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='newfeedback',
            name='s3_teacher_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]