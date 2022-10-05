from django.shortcuts import redirect, render
from django.contrib import messages
from seller.models import RawProduct, Seller, SellerProfileCheck
from app.models import Product
from .decorators import allowed_users
from seller.forms import ItemAdditionForm
from django.db.models import Q



@allowed_users(allowed_roles=['moderators'])
def moderator_page(request):
    return render(request, 'homepage.html')

@allowed_users(allowed_roles=['moderators'])
def searchbar(request):
    if request.method=="GET":
        search = request.GET.get("search")
        product = Product.objects.filter(Q(name__icontains=search))
        return render(request, 'app/searchbar.html', {'product':product})


@allowed_users(allowed_roles=['moderators'])
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})


@allowed_users(allowed_roles=['moderators'])
def pending_products(request):
    pending = Product.objects.filter(is_verified=False)
    return render(request, 'pending_products.html', {'pending': pending})


@allowed_users(allowed_roles=['moderators'])
def all_products(request):
    products = Product.objects.filter(is_verified=True)
    return render(request, 'all_products.html', {'products': products})


@allowed_users(allowed_roles=['moderators'])
def review_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'review_product.html', {"p": product})


@allowed_users(allowed_roles=['moderators'])
def approve(request, id):
    product = Product.objects.get(id=id)
    product.is_verified = True
    product.save()
    return redirect('moderator:pending-products')


@allowed_users(allowed_roles=['moderators'])
def disapprove(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('moderator:pending-products')


@allowed_users(allowed_roles=['moderators'])
def pending_seller(request):
    pending = SellerProfileCheck.objects.all()
    return render(request, 'pending_seller.html', {'pending': pending})
