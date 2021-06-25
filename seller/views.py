from app.views import login
from django.shortcuts import redirect, render
from django.contrib import messages
from . models import SellerProduct, Seller, RawProduct
from app.models import Product, Confirmation
from . forms import ItemAdditionForm, SellerAdditionForm
from django.contrib.auth.decorators import login_required


@login_required
def seller(request):
    user = request.user
    return render(request, 'seller/core/index.html')


@login_required
def listings(request):
    products = Product.objects.filter(seller=request.user.id, is_verified=True)
    print(products)
    if products:
        return render(request, 'seller/listings.html', {'products': products})
    else:
        return render(request, 'seller/emptylisting.html')


@login_required
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
            messages.success(
                request, "Item saved for confirmation.")
            product.save()
    else:
        form = ItemAdditionForm()
    return render(request, 'seller/add_items.html', {'form': form})


@login_required
def add_seller_profile(request):
    if request.method == 'POST':
        form = SellerAdditionForm(request.POST)
        if form.is_valid():
            user = request.user
            brand = request.POST.get('brand')
            shop = request.POST.get('shop')
            contact = request.POST.get('contact_number')
            seller = Seller(user=user, brand=brand,
                            shop=shop, contact_number=contact)
            messages.success(
                request, "New Seller profile saved for confirmation.")
            seller.save()
    else:
        form = SellerAdditionForm()
    return render(request, 'seller/add_seller_profile.html', {'form': form})


@login_required
def seller_profile(request):
    user = request.user
    sellers = Seller.objects.filter(user=user)
    return render(request, 'seller/seller_profile.html', {'sellers': sellers})


@login_required
def order_placed(request):
    user = request.user
    confirmations = Confirmation.objects.filter(seller_id=user.id).order_by('id').reverse()
    if confirmations:
        return render(request, 'seller/order_placed.html', {'confirmations': confirmations})
    else:
        return render(request, 'seller/no_confirmations.html')


@login_required
def pending_listings(request):
    products = Product.objects.filter(seller=request.user.id,is_verified=False)
    return render(request, 'seller/pending.html', {'products': products})

@login_required
def change_status(request, id):
    product = Confirmation.objects.get(id=id)
    product.order_status = request.POST.get('status')
    print(product.order_status)
    product.save()
    return redirect('seller:order-placed')

@login_required
def product_detail(request, id):
    confirmation = Confirmation.objects.get(id=id)
    return render(request, 'seller/product_detail.html', {'c':confirmation})