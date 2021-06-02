from django.db import models
from django.contrib.auth.models import User

Category_choices = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('BW', 'Bottom Wear'),
    ('TW', 'Top Wear')
)


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    discountedPrice = models.FloatField()
    category = models.CharField(choices=Category_choices, max_length=3)
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productimg')
    seller = models.IntegerField(default="00")

    def __str__(self):
        return str(self.id)


STATE_CHOICES = (
    ('ANDHRA PRADESH', 'ANDHRA PRADESH'),
    ('ARUNANCHAL PRADESH', 'ARUNANCHAL PRADESH'),
    ('ASSAM', 'ASSAM'),
    ('BIHAR', 'BIHAR'),
    ('CHATTISGARH', 'CHATTISGARH'),
    ('GOA', 'GOA'),
    ('GUJRAT', 'GUJRAT'),
    ('HARYANA', 'HARYANA'),
    ('HIMANCHAL PRADESH', 'HIMANCHAL PRADESH'),
    ('JHARKHAND', 'JHARKHAND'),
    ('KARNATAKA', 'KARNATAKA'),
    ('KERALA', 'KERALA'),
    ('MADHYA PRADESH', 'MADHYA PRADESH'),
    ('MAHARASTRA', 'MAHARASTRA'),
    ('MANIPUR', 'MANIPUR'),
    ('ODISHA', 'ODISHA'),
    ('PUNJAB', 'PUNJAB'),
    ('RAJASTHAN', 'RAJASTHAN'),
    ('TAMIL NADU', 'TAMIL NADU'),
    ('TELANGANA', 'TELANGANA'),
    ('UTTAR PRADESH', 'UTTAR PRADESH'),
    ('UTTARAKHAND', 'UTTARAKHAND'),
    ('WEST BENGAL', 'WEST BENGAL')
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'customer'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "cart"

    @property
    def total_cost(self):
        return self.quantity * self.product.discountedPrice


STATUS_CHOICES = (
    ('PENDING', 'PENDING'),
    ('ACCEPTED', 'ACCEPTED'),
    ('PACKED', 'PACKED'),
    ('SHIPPED', 'SHIPPED'),
    ('ON THE WAY', 'ON THE WAY'),
    ('DELIVERED', 'DELIVERED')
)


class Confirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        choices=STATUS_CHOICES, max_length=50, default='PENDING')
    seller_id = models.CharField(max_length=10, default="000")

    class Meta:
        verbose_name_plural = "confirmation"

    @property
    def total_cost(self):
        return self.quantity * self.product.discountedPrice



