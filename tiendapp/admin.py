from django.contrib import admin
from tiendapp.models import Product, Category, ProductCategory
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductCagoryAdmin(admin.ModelAdmin):
    pass