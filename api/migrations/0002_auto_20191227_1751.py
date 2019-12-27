# Generated by Django 3.0.1 on 2019-12-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='app_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=300)),
                ('app_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('updated', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('installs', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=40)),
                ('android', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='app_deatils',
        ),
    ]
