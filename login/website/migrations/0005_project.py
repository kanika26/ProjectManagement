# Generated by Django 3.0.2 on 2020-01-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200122_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False)),
                ('Pname', models.CharField(max_length=500)),
                ('Pdescription', models.CharField(max_length=3000)),
                ('Cname', models.CharField(max_length=300)),
                ('Cdetails', models.CharField(max_length=4000)),
                ('Pdeadline', models.CharField(max_length=100)),
                ('Pstartdate', models.CharField(max_length=100)),
                ('Pmanagedby', models.CharField(max_length=400)),
                ('Pcontract', models.CharField(max_length=2000)),
                ('Ptextresource', models.CharField(max_length=6000)),
                ('Pstatus', models.IntegerField()),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
