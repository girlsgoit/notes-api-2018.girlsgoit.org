# Generated by Django 2.0.7 on 2018-07-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_merge_20180717_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
