# Generated by Django 2.0.5 on 2018-09-04 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lowuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseno', models.CharField(max_length=20)),
                ('expirydate', models.DateField()),
                ('type', models.IntegerField()),
                ('issuedate', models.DateField()),
                ('licenseid', models.OneToOneField(on_delete=True, to='lowuser.userdb')),
            ],
        ),
        migrations.CreateModel(
            name='marriagecert',
            fields=[
                ('certno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('regoffid', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('waadhar', models.CharField(max_length=13)),
                ('saadhar', models.CharField(max_length=13)),
                ('marriageid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lowuser.userdb')),
            ],
        ),
        migrations.CreateModel(
            name='pancard',
            fields=[
                ('panno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('majorstatus', models.IntegerField()),
                ('pancardid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lowuser.userdb')),
            ],
        ),
        migrations.CreateModel(
            name='passport',
            fields=[
                ('dateissue', models.DateField()),
                ('passportno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nationality', models.CharField(max_length=30)),
                ('dateexpiry', models.DateField()),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('passportid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lowuser.userdb')),
            ],
        ),
        migrations.CreateModel(
            name='votercard',
            fields=[
                ('voterid', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('voter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lowuser.userdb')),
            ],
        ),
    ]
