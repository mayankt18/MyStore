from rest_framework import viewsets 
from app.models import Product 
from .serializers import ProductSerializer , UserSerializer 
from django.contrib.auth.models import User 
from rest_framework import permissions
from . permissions import IsModeratorOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_verified=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsModeratorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.id)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
