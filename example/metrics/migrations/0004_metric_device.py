# Generated by Django 3.1.4 on 2020-12-22 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20201222_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='device',
            field=models.IntegerField(default=0),
        ),
    ]
