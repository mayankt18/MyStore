# Generated by Django 3.2.2 on 2021-05-29 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_product_discountedprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('store_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('BW', 'Bottom Wear'), ('TW', 'Top Wear')], max_length=3)),
                ('address', models.CharField(max_length=300)),
                ('shipping_method', models.CharField(choices=[('FULFILLED BY MyStore', 'FULFILLED BY MyStore'), ('MyStore EASY SHIP', 'MyStore EASY SHIP'), ('SELF-SHIP', 'SELF-SHIP')], max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.confirmation')),
                ('listed_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]