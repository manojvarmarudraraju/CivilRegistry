# Generated by Django 2.0.5 on 2018-10-07 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lowuser', '0004_userdb_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pincodelog',
            name='pinl',
        ),
        migrations.DeleteModel(
            name='pincodelog',
        ),
    ]
