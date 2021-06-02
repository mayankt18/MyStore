from seller.models import SellerProduct,Seller
from app.models import Product
from django import forms
from app.models import Category_choices

class SellerAdditionForm(forms.ModelForm):
    brand = forms.CharField(max_length=200,label="Brand", widget=forms.TextInput(attrs={'class':'input'}))
    shop = forms.CharField(max_length=200,label="Shop", widget=forms.TextInput(attrs={'class':'input'}))
    contact_number = forms.CharField(max_length=10,label="Contact Number", widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ['user']


class ItemAdditionForm(forms.ModelForm):
    name = forms.CharField(max_length=300, label="Name", widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class':'input'}))
    price = forms.FloatField(label="Price", widget=forms.NumberInput(attrs={'class':'input'}))
    discountedPrice = forms.FloatField(label="Discounted Price", widget=forms.NumberInput(attrs={'class':'input'}))
    category = forms.ChoiceField(label="Category", widget=forms.Select(), choices=Category_choices)
    brand = forms.CharField(label="Brand", widget=forms.TextInput(attrs={'class':'input'}))
    image = forms.ImageField(label="Image", widget=forms.FileInput(attrs={'class':'input'}))
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user','seller','product']
   
