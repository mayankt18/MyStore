from rest_framework import viewsets 
from app.models import Product 
from .serializers import ProductSerializer , UserSerializer 
from django.contrib.auth.models import User 

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_verified=True)
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

