# Generated by Django 3.0.6 on 2020-05-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_modelredirecturl'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelredirecturl',
            name='roles_responsibility',
            field=models.BooleanField(default=False),
        ),
    ]