from django.db import models
from django.contrib.auth.models import User
from app.models import Product


class Seller(models.Model):
    is_verified = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    shop = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class SellerProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


Category_choices = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('BW', 'Bottom Wear'),
    ('TW', 'Top Wear')
)


class RawProduct(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    discountedPrice = models.FloatField()
    category = models.CharField(choices=Category_choices, max_length=3)
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productimg')
    seller = models.IntegerField(default="00")

    def __str__(self):
        return str(self.id)


class SellerProfileCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    shop = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)
