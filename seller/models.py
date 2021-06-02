from django.db import models
from django.contrib.auth.models import User
from app.models import Product

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    shop = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

class SellerProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)

   