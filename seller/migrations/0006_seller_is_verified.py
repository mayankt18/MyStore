# Generated by Django 3.2.4 on 2021-06-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_sellerprofilecheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]