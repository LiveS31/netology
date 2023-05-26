from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    notes = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders',
                                      through='OrderItems')

# В классе META- входят вносятся данные, которые относятся ко всех таблици
#предположим делаем сортировку по имени

# и выводим все это на экран
    def __str__(self):
        return f'Заказ №: {self.id}'
# связующая таблица
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT,
                              related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=1)


# Чтобы нельзя было добавить один и тот же товар
    class Meta:
        unique_together = ('order', 'product') #сочитание будет всегда уникально
    def __str__(self):
        return f'{self.product.name}, {self.quantity}шт.'

