from django.contrib import admin
from .models import Category, Customer, Order, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)