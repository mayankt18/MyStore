from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . models import Product, Customer, Confirmation, Cart
from .forms import *
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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
    user = request.user
    carted_item = False
    if user.is_authenticated:
        carted_item = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request, 'app/productinfo.html', {'p':product, 'carted_item':carted_item})


def products(request, tag=None):
    if tag==None:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(category=tag)
    return render(request, 'app/product.html', {'product':product})

def searchbar(request):
    if request.method=="GET":
        search = request.GET.get("search")
        product = Product.objects.filter(Q(name__icontains=search))
        return render(request, 'app/searchbar.html', {'product':product})


def login(request):
    return render(request, 'app/user/login.html')


def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request, "Congratulations !!! New Account created successfully :)")
            form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request, 'app/user/register.html', {'form':form})


@method_decorator(login_required,name="dispatch")
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/user/profile.html', {'form':form,'active':'btn-warning'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user= usr, locality=locality,city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile updated Successfully!!!')
        return render(request, 'app/user/profile.html', {'form':form, 'active':'btn-warning'})

@login_required
def addressview(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/user/address.html', {'active':'btn-warning', 'add':add})

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('app:product-detail', id=product_id)


@login_required
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_price = 40.00
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discountedPrice
                amount = amount + tempamount
                total_amount = amount + shipping_price
            return render(request, 'app/cart/show_cart.html', {'cart':cart, 'total':total_amount, 'amount':amount})
        else:
            return render(request, 'app/cart/emptycart.html')


@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        amount = 0.0
        shipping_price = 40.00
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discountedPrice
            amount = amount + tempamount
            
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': amount + shipping_price
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -=1
        c.save()
        amount = 0.0
        shipping_price = 40.00
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discountedPrice
            amount = amount + tempamount
            
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_price
        }
        return JsonResponse(data)


@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_price = 40.00
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = p.quantity * p.product.discountedPrice
            amount = amount + tempamount
            
        data = {
            'amount':amount,
            'totalamount':amount + shipping_price
        }
        return JsonResponse(data)


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    if add:
        cart_item = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_price = 40.00
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discountedPrice
                amount = amount + tempamount
            data={'amount':amount,
                'shipping': shipping_price,
                'totalamount': amount + shipping_price
            }
        return render(request, 'app/cart/checkout.html', {'add':add, 'data':data, 'cart_items':cart_item})
    else:
        return redirect('app:profile')


@login_required
def confirmation(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Confirmation(user=user, customer=customer, product=c.product, quantity=c.quantity, 
        seller_id=c.product.seller).save()
        c.delete()

    return redirect("app:orders")


@login_required
def orders(request):
    op = Confirmation.objects.filter(user=request.user)
    return render(request, 'app/cart/orders.html', {'op':op})



# categories = Category.objects.all()
# all_products = []
#     for category in categories:
#         products = Product.objects.filter(category=category)
#         all_products.append({'products': products, 'category':category])
#     context = {
#        'all_products': all_products,
#     }