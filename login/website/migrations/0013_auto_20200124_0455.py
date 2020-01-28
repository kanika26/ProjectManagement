# Generated by Django 3.0.2 on 2020-01-24 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200123_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='empid',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='Tassignedto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.userlogin'),
        ),
    ]
