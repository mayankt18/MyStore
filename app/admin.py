from django.contrib import admin
from .models import Product, Customer, Cart, Confirmation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','discountedPrice',
                    'category','brand','image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','order_date','order_status']

