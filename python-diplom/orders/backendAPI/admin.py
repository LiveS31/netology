from django.contrib import admin

# Register your models here.
from .models import User, Contact, ConfirmEmailToken, Shop, Category, Product, Parameter,\
    ProductParameter, Order, OrderItem

@admin.register(User)
class UserAmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'site', 'state']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price_rrc', 'category']


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'value']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contact', 'created', 'status']
    list_filter = ['created', 'status', 'user']
    list_editable = ['status']
    fields = (('user', 'contact'), ('created', 'updated'), 'status')
    readonly_fields = ('created', 'updated')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','total_amount', 'shop']
