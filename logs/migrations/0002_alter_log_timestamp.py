# Generated by Django 3.2.3 on 2021-05-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
