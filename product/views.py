from django.contrib import messages
from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
	template = "product/products2.html"
	products = Product.objects.filter(active=True)
	context = {
		"section": "products",
		"products": products,
	}
	return render(request, template, context)


def product_detail(request, slug):
	template = "product/product_detail.html"
	try:
		product = Product.objects.get(slug=slug)
	except:
		product = None
	if product:
		context = {
			"section": "products",
			"product": product,
		}
		return render(request, template, context)
	return render(request, "product/404.html")


def product_search(request):
	try:
		query = request.GET.get("q")
		products = Product.objects.filter(title__contains=query)
	except:
		query = None
		products = Product.objects.filter(title__contains=query)
	if products:
		template = "product/products2.html"
		messages.success(request, "Your search results......")
		context = {
			"products": products,
		}
		return render(request, template, context)
	return render(request, "product/404.html")
