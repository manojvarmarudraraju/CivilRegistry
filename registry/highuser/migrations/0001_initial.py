# Generated by Django 2.0.5 on 2018-09-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.CharField(max_length=13)),
                ('userid', models.CharField(max_length=13)),
                ('veridate', models.DateField()),
            ],
        ),
    ]
