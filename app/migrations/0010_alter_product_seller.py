# Generated by Django 3.2.2 on 2021-06-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.IntegerField(default='00'),
        ),
    ]
