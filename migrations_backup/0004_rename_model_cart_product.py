# Generated by Django 4.2.1 on 2023-06-20 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='model',
            new_name='product',
        ),
    ]
