# Generated by Django 3.2.2 on 2021-06-02 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sellerproduct',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='sellerproduct',
            name='user',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
        migrations.DeleteModel(
            name='SellerProduct',
        ),
    ]