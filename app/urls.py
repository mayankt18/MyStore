from app.forms import LoginForm
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('product-detail/<int:id>', views.product_detail, name="product-detail"),
    path('products', views.products, name="products"),
    path('products/<slug:tag>', views.products, name="filter-products"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/user/login.html",
    authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name="logout"),
    path('register/', views.register, name="register"),
    path('accounts/profile/', views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
