from django.shortcuts import render
from django.contrib import messages
from . models import SellerProduct, Seller
from app.models import Product, Confirmation
from . forms import ItemAdditionForm,SellerAdditionForm

def seller(request):
    user = request.user
    return render(request, 'seller/core/Bell/index.html')


def listings(request):
    products = Product.objects.filter(seller=request.user.id)
    print(products)
    if products:
        return render(request, 'seller/listings.html', {'products':products})
    else:
        return render(request, 'seller/emptylisting.html')


def add_items(request):
    if request.method == 'POST':
        form = ItemAdditionForm(request.POST, request.FILES)
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discountedPrice = request.POST.get('discountedPrice')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        image = request.FILES['image']
        print(image)
        if form.is_valid():
            product = Product(name=name, description=description, price=price, discountedPrice=discountedPrice,
                category=category, brand=brand, image=image, seller=request.user.id)
            messages.success(request, "Congratulations !!! New Item added successfully :)")
            product.save()
    else:
        form = ItemAdditionForm()
    return render(request, 'seller/add_items.html',{'form':form})


def add_seller_profile(request):
    if request.method=='POST':
        form = SellerAdditionForm(request.POST)
        if form.is_valid():
            user = request.user.id
            brand = request.POST.get('brand')
            shop = request.POST.get('shop')
            contact = request.POST.get('contact_number')
            seller = Seller(user=user, brand=brand, shop=shop, contact_number=contact)
            messages.success(request, "Congratulations New Seller profile added.")
            seller.save()
    else:
        form = SellerAdditionForm()
    return render(request, 'seller/add_seller_profile.html',{'form':form})


def seller_profile(request):
    user = request.user
    sellers = Seller.objects.filter(user=user)
    return render(request, 'seller/seller_profile.html', {'sellers':sellers}) 


def order_placed(request):
    user = request.user
    confirmations = Confirmation.objects.filter(seller_id=user.id)
    if confirmations:
        return render(request, 'seller/order_placed.html', {'confirmations':confirmations})
    else:
        return render(request, 'seller/no_confirmations.html')
