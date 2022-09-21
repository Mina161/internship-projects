# Generated by Django 4.1.1 on 2022-09-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('device_type', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
            ],
        ),
    ]
