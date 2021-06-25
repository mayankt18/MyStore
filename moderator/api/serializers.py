from rest_framework import serializers 
from app.models import Product
from django.contrib.auth.models import User 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','discountedPrice',
        'category','brand','image','seller']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

        