from django.contrib import admin

# Register your models here.
from .models import ProductType, Product, Order

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Order)