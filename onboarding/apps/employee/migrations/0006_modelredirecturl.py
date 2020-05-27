# Generated by Django 3.0.6 on 2020-05-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20200526_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelRedirectUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.BooleanField(default=False)),
                ('family_info', models.BooleanField(default=False)),
                ('emergency_contact', models.BooleanField(default=False)),
                ('document_gathering', models.BooleanField(default=False)),
                ('drug_declaration', models.BooleanField(default=False)),
                ('bank_detail', models.BooleanField(default=False)),
                ('user', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Redirect Url',
                'verbose_name_plural': 'Redirect Url',
                'db_table': 'redirect_url',
                'managed': True,
            },
        ),
    ]