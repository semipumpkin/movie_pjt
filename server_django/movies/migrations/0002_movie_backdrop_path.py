# Generated by Django 3.2.3 on 2021-05-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
