# Generated by Django 3.0.2 on 2020-01-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20200124_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Tassignedto',
            field=models.IntegerField(),
        ),
    ]
