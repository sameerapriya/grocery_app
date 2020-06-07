from django.db import models
from django.contrib.auth import get_user_model

order_status = ((0, 'unfulfilled'),(1, 'fulfilled'),(2,'cancelled'),(3,'refunded'))


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=order_status, default=0)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    email = models.EmailField()
    checkout_token = models.CharField(max_length=36, default="")
    note = models.TextField(blank=True,default="")

    def __str__(self):
        return self.email


class OrderLine(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, editable=False)
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    sku = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{self.product_name}x{self.product_price}'
