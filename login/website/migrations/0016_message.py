# Generated by Django 3.0.2 on 2020-01-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200124_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('Mid', models.AutoField(primary_key=True, serialize=False)),
                ('sender_username', models.CharField(max_length=3000)),
                ('receiver_username', models.CharField(max_length=3000)),
                ('content', models.CharField(max_length=45000)),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]