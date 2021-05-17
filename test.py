from app.models import Product

product = Product.objects.filter(category='M')

for p in product:
    print(p.categroy)
