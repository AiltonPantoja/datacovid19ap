# Generated by Django 3.0.5 on 2020-04-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvupload',
            name='completo',
            field=models.BooleanField(default=False),
        ),
    ]
