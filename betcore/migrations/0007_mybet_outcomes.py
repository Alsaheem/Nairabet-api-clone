# Generated by Django 3.0.5 on 2020-04-08 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betcore', '0006_auto_20200407_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybet',
            name='outcomes',
            field=models.ManyToManyField(to='betcore.Outcome'),
        ),
    ]