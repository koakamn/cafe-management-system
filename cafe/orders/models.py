from django.db import models
from menu.models import Product

class Order(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,
                            related_name='items')

    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name}*{self.quantity}'
