from django.shortcuts import render
from django.http import HttpResponse
from . models import *


def homepage(request):
    bottomwear = Product.objects.filter(category="BW")
    topwear = Product.objects.filter(category="TW")
    mobiles = Product.objects.filter(category="M")
    laptops = Product.objects.filter(category="L")
    context = {'Mobiles':mobiles,
                'Laptops':laptops,
                'Topwear':topwear,
                'Bottomwear':bottomwear}
    return render(request, 'app/homepage.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'app/productinfo.html', {'p':product})

def mobiles(request):
    mobiles = Product.objects.filter(category="M")
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

def products(request, tag=None):
    if tag==None:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(category=tag)
    return render(request, 'app/product.html', {'product':product})
