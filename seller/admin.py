from django.contrib import admin
from . models import RawProduct, Seller, SellerProduct


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'brand', 'shop',
                    'contact_number']


@admin.register(SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seller', 'product']


@admin.register(RawProduct)
class RawProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discountedPrice',
                    'category', 'brand', 'image']
