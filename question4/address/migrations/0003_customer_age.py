# Generated by Django 3.1.4 on 2020-12-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20201226_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]