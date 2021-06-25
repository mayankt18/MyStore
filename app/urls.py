from app.forms import LoginForm, ChangePasswordForm, MyPasswordResetForm, MySetPasswordForm
from django.urls import path, reverse_lazy, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


app_name="app"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    
    path('product-detail/<int:id>', views.product_detail, name="product-detail"),
    
    path('products', views.products, name="products"),

    path('search/', views.searchbar, name="searchbar"),
    
    path('products/<slug:tag>', views.products, name="filter-products"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/user/login.html",
    authentication_form=LoginForm), name="login"),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='app:login'), name="logout"),
    
    path('register/', views.register, name="register"),
    
    path('accounts/profile/', views.ProfileView.as_view(), name="profile"),

    path('account/address/', views.addressview, name="address"),
    
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='app/user/changepassword.html',
    form_class=ChangePasswordForm, success_url='/password-changed/'), name="change-password"),
    
    path('password-changed/', auth_views.PasswordChangeDoneView.as_view(template_name='app/user/passwordchangesuccess.html'),
    name='password-change-success'),

    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),

    path('cart/', views.cart, name="cart"),

    path('pluscart/', views.plus_cart),

    path('minuscart/', views.minus_cart),

    path('removecart/', views.remove_cart),

    path('checkout/', views.checkout, name="checkout"),

    path('confirmation/', views.confirmation, name="confirmation"),

    path('orders', views.orders, name="orders"),

    path('redirecter/', views.redirecter, name="redirecter"),

    path('buy_now/<int:id>', views.buy_now, name="buy-now"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
