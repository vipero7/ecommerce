# Generated by Django 2.0.5 on 2019-09-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]
