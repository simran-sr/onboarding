# Generated by Django 3.0.6 on 2020-05-22 07:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelEmployee',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, help_text='Unique identification for an account.', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
                'managed': True,
            },
        ),
    ]
