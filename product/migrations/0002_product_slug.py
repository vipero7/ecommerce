# Generated by Django 2.0.5 on 2019-09-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]
