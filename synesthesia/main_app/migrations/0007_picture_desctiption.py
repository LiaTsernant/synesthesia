# Generated by Django 3.0.4 on 2020-03-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200318_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='desctiption',
            field=models.TextField(default='Blurb', max_length=500),
        ),
    ]
