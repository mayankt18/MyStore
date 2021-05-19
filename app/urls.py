from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('product-detail/<int:id>', views.product_detail, name="product-detail"),
    path('mobiles/', views.mobiles, name="mobiles"),
    path('products', views.products, name="products"),
    path('products/<slug:tag>', views.products, name="filter-products"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
