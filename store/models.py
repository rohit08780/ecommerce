from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)