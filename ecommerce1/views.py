from django.contrib import messages
from django.shortcuts import render

from product.models import Product


def index(request):
	template = "product/products2.html"
	products = Product.objects.filter(active=True)
	context = {
		"section": "products",
		"products": products,
	}
	messages.success(request, "Hello there")
	return render(request, template, context)


def contact(request):
	template = "contact.html"
	context = {
		"section": "products",
	}
	return render(request, template, context)