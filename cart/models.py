from django.db import models

# Create your models here.
from product.models import Product

class Item(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

	quantity = models.IntegerField(default=1)
	item_total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product.title


class Cart(models.Model):
	# items = models.ManyToManyField(CartItem, null=True, blank=True)
	cart_total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return "Cart id: %s" % self.id