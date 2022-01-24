from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'image']

admin.site.register(Product, AdminProduct)


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, AdminCategory)


class AdminCutomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email','password']

admin.site.register(Customer, AdminCutomer)
