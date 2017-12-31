from django.db import models
from cart.models import Cart
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

STATUS_CHOICES = (
	("Started", "Started"),
	("Abandoned", "Abandoned"),
	("Finished", "Finished"),
)

class Order(models.Model):
	# address*
	order_id = models.CharField(max_length=120, default="ABCD", unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
	tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
	final_price_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="started")
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.order_id


