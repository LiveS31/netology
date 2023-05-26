from django.contrib import admin

# Register your models here.
#импортируем из moduls
from .models import Category, OrderItems, Order, Product


class OrderItemsInline(admin.TabularInline):
    model = OrderItems #Сама модель
    filter = ['product', 'quantity'] #поля продукт и количество
    extra = 0 # количество полей по умолчанию в админке

#Для того, чтобы можно было добовлять заказы сразу,
# а не каждый раз закодить
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline] # нужно зарегистривоть

#Регистрируем классы которые и есть таблица
#после этого модели должны появиться в админе
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
#admin.site.register(OrderItems)
admin.site.register(Product)
