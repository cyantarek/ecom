from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .models import Order
from cart.models import Cart
from django.urls import reverse
from .utils import get_order_id

# Create your views here.

@login_required
def orders(request):
	context = {

	}
	template = "order/orders.html"

	return render(request, template, context)

@login_required
def checkout(request):
	try:
		cart_id = request.session["cart_id"]
		cart = Cart.objects.get(id=cart_id)
	except:
		cart_id = None
		return HttpResponseRedirect(reverse("cart"))

	try:
		order = Order.objects.get(cart=cart)
	except:
		order = Order.objects.create(cart=cart)
		order.order_id = get_order_id()
		order.user = request.user
		order.save()

	if order.status == "Finished":
		del request.session["cart_id"]
		del request.session["total_items"]
		cart.delete()

	context = {
		"cart": cart,
		"order": order,
	}
	template = "order/checkout.html"

	return render(request, template, context)