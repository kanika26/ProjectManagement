# Generated by Django 3.0.2 on 2020-01-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20200124_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Mid',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver_username',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender_username',
        ),
        migrations.AddField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=300),
        ),
    ]