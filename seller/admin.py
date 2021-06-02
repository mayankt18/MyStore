from django.contrib import admin
from . models import Seller, SellerProduct

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id','user','brand','shop',
                    'contact_number']



@admin.register(SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','seller','product']
