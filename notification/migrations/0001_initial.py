# Generated by Django 2.1.3 on 2018-11-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]