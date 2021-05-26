from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from .forms import *
from django.contrib import messages
from django.views import View


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


def products(request, tag=None):
    if tag==None:
        product = Product.objects.all()
    else:
        product = Product.objects.filter(category=tag)
    return render(request, 'app/product.html', {'product':product})


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
