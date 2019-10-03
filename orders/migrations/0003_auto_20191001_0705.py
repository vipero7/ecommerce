# Generated by Django 2.0.5 on 2019-10-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_userorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='progress',
            field=models.CharField(choices=[('P', 'Pending'), ('PP', 'Processing'), ('S', 'Shipped')], default='P', max_length=10),
        ),
    ]