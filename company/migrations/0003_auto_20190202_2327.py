# Generated by Django 2.1.5 on 2019-02-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20190202_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registar',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
