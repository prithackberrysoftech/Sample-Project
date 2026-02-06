from django.db import models
from django.contrib.auth.models import User
import uuid

# class User(AbstractUser):
#     pass

class Product(models.Model):
    name = models.CharField(max_length=50, help_text="Add Your Product Name")
    description = models.TextField(blank=True,null=True)
    price =  models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product")

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED  = 'Confirmed'
        CANCELLED = 'CANCELLED'

    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User, verbose_name=("orders"), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=StatusChoice,default=StatusChoice.PENDING)
    product =  models.ManyToManyField(Product, through='OrderItem' ,related_name='orders')

    def __str__(self):
        return f"Order {self.order_id} By {self.user.username}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name="items")
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    @property
    def item_subtotal(self):
        return self.product.price  * self.quantity
    

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in Order {self.order.order_id}"