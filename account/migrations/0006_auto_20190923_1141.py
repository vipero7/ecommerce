# Generated by Django 2.0.5 on 2019-09-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190923_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
