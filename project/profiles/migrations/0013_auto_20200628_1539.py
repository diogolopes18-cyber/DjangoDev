# Generated by Django 2.0.7 on 2020-06-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20200628_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userform',
            name='feautured',
        ),
        migrations.RemoveField(
            model_name='userform',
            name='title',
        ),
        migrations.AddField(
            model_name='userform',
            name='password',
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userform',
            name='username',
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
    ]
