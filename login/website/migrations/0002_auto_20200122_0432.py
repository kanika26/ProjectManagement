# Generated by Django 3.0.2 on 2020-01-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userlogin',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
