# Generated by Django 3.0.2 on 2020-01-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200122_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('Tid', models.AutoField(primary_key=True, serialize=False)),
                ('Ttitle', models.CharField(max_length=3000)),
                ('Pid', models.IntegerField()),
                ('Tstatus', models.IntegerField()),
                ('Ttechnology', models.CharField(choices=[('JAVA', 'JAVA'), ('PYTHON', 'PYTHON'), ('MATLAB', 'MATLAB'), ('JULIA', 'JULIA'), ('R', 'R')], max_length=100)),
                ('Tassignedto', models.CharField(max_length=600)),
                ('Tassignedby', models.CharField(max_length=600)),
                ('Tassigneddate', models.CharField(max_length=600)),
                ('Tdeadline', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
