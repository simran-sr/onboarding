# Generated by Django 3.0.6 on 2020-05-22 09:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelemployee',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identification for an account.', primary_key=True, serialize=False),
        ),
    ]