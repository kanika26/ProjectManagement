# Generated by Django 3.0.2 on 2020-01-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Tassignedto',
            field=models.IntegerField(),
        ),
    ]
