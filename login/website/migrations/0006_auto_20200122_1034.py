# Generated by Django 3.0.2 on 2020-01-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Pdeadline',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='Pstartdate',
            field=models.DateField(max_length=100),
        ),
    ]