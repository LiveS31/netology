from django.contrib import admin

#Register your models here.

from .models import Product, Stock, StockProduct
# регистрируем для админки

@admin.register(Product) # регистрируем Product
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock) # регистрируем Stock
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(StockProduct) # регистрируем StockProduct
class StockProductAdmin(admin.ModelAdmin):
    pass