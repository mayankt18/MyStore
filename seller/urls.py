from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "seller"

urlpatterns = [
    path('', views.seller, name="seller"),

    path('listings/', views.listings, name="listings"),

    path('add_items/', views.add_items, name="add-items"),

    path('add_seller_profile/', views.add_seller_profile,
         name="add-seller-profile"),

    path('seller_profile/', views.seller_profile, name="seller-profile"),

    path('order_placed/', views.order_placed, name="order-placed"),

    path('pending_listings/', views.pending_listings, name="pending-listings")

]
