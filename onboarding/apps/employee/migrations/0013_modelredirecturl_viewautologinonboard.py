# Generated by Django 3.0.6 on 2020-06-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_auto_20200601_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelredirecturl',
            name='ViewAutoLoginOnboard',
            field=models.BooleanField(default=True),
        ),
    ]