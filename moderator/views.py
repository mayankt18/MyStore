from django.shortcuts import redirect, render
from django.contrib import messages
from seller.models import RawProduct, Seller, SellerProfileCheck
from app.models import Product
from .decorators import allowed_users
from seller.forms import ItemAdditionForm


@allowed_users(allowed_roles=['moderators'])
def moderator_page(request):
    return render(request, 'homepage.html')


@allowed_users(allowed_roles=['moderators'])
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})


@allowed_users(allowed_roles=['moderators'])
def pending_products(request):
    pending = RawProduct.objects.all()
    return render(request, 'pending_products.html', {'pending': pending})


@allowed_users(allowed_roles=['moderators'])
def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


@allowed_users(allowed_roles=['moderators'])
def review_product(request, id):
    if request.method == "POST":
        form = ItemAdditionForm(request.POST, request.FILES)
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discountedPrice = request.POST.get('discountedPrice')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        seller = request.POST.get('seller')
        image = request.POST.get('image')[7:]
        print(image)
        if form.is_valid:
            product = Product(name=name, description=description, price=price, discountedPrice=discountedPrice,
                              category=category, brand=brand, image=image, seller=seller)
            messages.success(
                request, "Congratulations !!! New Item added successfully :)")
            product.save()
            rproduct = RawProduct.objects.get(id=id)
            rproduct.delete()
        else:
            print("___form invalid!!!___")

    else:
        product = RawProduct.objects.get(id=id)
    return render(request, 'review_product.html', {"p": product})


@allowed_users(allowed_roles=['moderators'])
def disapprove(request, id):
    product = RawProduct.objects.get(id=id)
    product.delete()
    return redirect('moderator:pending-products')


@allowed_users(allowed_roles=['moderators'])
def pending_seller(request):
    pending = SellerProfileCheck.objects.all()
    return render(request, 'pending_seller.html', {'pending': pending})
