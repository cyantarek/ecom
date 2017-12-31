from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=29.99)
	sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=29.99, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_price(self):
		return self.price


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(blank=True, upload_to="products/images/")
	featured = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	thumbnail = models.BooleanField(default=False)

	def __str__(self):
		return self.product.title + " " + str(self.id)