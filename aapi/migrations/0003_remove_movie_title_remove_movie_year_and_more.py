# Generated by Django 4.2.2 on 2023-07-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aapi', '0002_movie_delete_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.CharField(max_length=10000),
        ),
    ]
