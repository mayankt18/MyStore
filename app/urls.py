from app.forms import LoginForm, ChangePasswordForm, MyPasswordResetForm, MySetPasswordForm
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    
    path('product-detail/<int:id>', views.product_detail, name="product-detail"),
    
    path('products', views.products, name="products"),

    path('search/', views.searchbar, name="searchbar"),
    
    path('products/<slug:tag>', views.products, name="filter-products"),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name="app/user/login.html",
    authentication_form=LoginForm), name="login"),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    
    path('register/', views.register, name="register"),
    
    path('accounts/profile/', views.ProfileView.as_view(), name="profile"),

    path('account/address/', views.addressview, name="address"),
    
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='app/user/changepassword.html',
    form_class=ChangePasswordForm, success_url='/password-changed/'), name="change-password"),
    
    path('password-changed/', auth_views.PasswordChangeDoneView.as_view(template_name='app/user/passwordchangesuccess.html'),
    name='password-change-success'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view
    (template_name='app/pwdrst/password_reset.html', form_class=MyPasswordResetForm), name="password-reset"),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view
    (template_name='app/pwdrst/password_reset_done.html'), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
    (template_name='app/pwdrst/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view
    (template_name='app/pwdrst/password_reset_complete.html'), name="password_reset_complete"),

    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),

    path('cart/', views.cart, name="cart"),

    path('pluscart/', views.plus_cart),

    path('minuscart/', views.minus_cart),

    path('removecart/', views.remove_cart),

    path('checkout/', views.checkout, name="checkout"),

    path('confirmation/', views.confirmation, name="confirmation"),

    path('orders', views.orders, name="orders")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
