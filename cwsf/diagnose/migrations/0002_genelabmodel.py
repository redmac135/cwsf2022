# Generated by Django 4.0.5 on 2022-07-03 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenelabModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
    ]
