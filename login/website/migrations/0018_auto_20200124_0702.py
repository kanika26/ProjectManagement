# Generated by Django 3.0.2 on 2020-01-24 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20200124_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Tassignedto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.userlogin'),
        ),
    ]
