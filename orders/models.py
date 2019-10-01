from django.db import models
from product.models import Product
from account.models import Profile

# Create your models here.
PROGRESS_CHOICES = (
    ('P', 'Pending'),
    ('PP', 'Processing'),
    ('S', 'Shipped'),
)
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    progress = models.CharField(max_length=10, choices=PROGRESS_CHOICES, default='P')

    class Meta:
        ordering = ('-created',)

    def __str__self(self):
        return 'Order {}' .format(self.id)

    def get_total_cost(self):
        return sum(item.get.cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}' .format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class UserOrders(models.Model):
    user_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)



