from django.urls import path
from . import views

app_name = "moderator"

urlpatterns = [
    path('', views.moderator_page, name="homepage"),

    path('seller_list/', views.seller_list, name="seller-list"),

    path('pending_products/', views.pending_products, name="pending-products"),

    path('all_products/', views.all_products, name="all-products"),

    path('review_product/<int:id>', views.review_product, name="review-product"),

    path('approve/<int:id>', views.approve, name="approve"),

    path('disapprove/<int:id>', views.disapprove, name="disapprove"),

    path('pending_seller/', views.pending_seller, name="pending-seller"),

    path('search/', views.searchbar, name="searchbar"),

]
