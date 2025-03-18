# Generated by Django 4.1.4 on 2023-05-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='subject_3_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject_3_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject_4_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject_4_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject_5_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject_5_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='subject_1_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='subject_2_marks',
            field=models.IntegerField(default=0),
        ),
    ]
