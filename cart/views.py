from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from product.models import Product
from .models import Cart, Item


# Create your views here.

def view(request):
	"""
	Viewing the cart process:

	1.user session checking and getting the cart, send it as context (old session)
	2. if not get, send no cart(new session)
	"""

	template = "cart/view.html"
	try:
		cart_id = request.session["cart_id"]
	except KeyError:
		cart_id = None

	if cart_id:
		cart = Cart.objects.get(id=cart_id)
		context = {
			"cart": cart
		}
	else:
		context = {
			"cart": None
		}

	return render(request, template, context)


def update_cart(request, slug):
	"""
	Rule - One cart per session, multiple items per cart, single product + multiple quantity per item

	when adding/removing any product to the cart, it has to do this things:
	A. user session checking and getting the cart or creating it
	1. checks who is the user and if he has a cart for his current session
	2. if the user has a cart in his running session (old session) get his cart by
		his cart_id from his running session
	3. if the user has no cart in his session(new session), create a cart, save it and store the cart in the current
		session for	further use

	B. adding/removing product
	1. get the product using the provided slug
	2. if the product is in any of the cart_item's product list, get it, if not, create it as cart item.
	3. then we get the product as cart item by getting it or creating it
	4. if this cart item is not present in the cart's items list(created), add the item to the current cart's item list
	5. it it presents(get), remove it

	C. Calculating the total price for the current cart and total items in the current cart
	1. each item in the cart's item list has single product, single price but with multiple quantity
	2. so, by looping through all the items in the product, we can calculate the total price by summing each of the
		product's price multiplied by quantity.
		So total price(cart) = sum(each_cart_item_product_price * product_quantity)
	3. save the total price for the cart
	4. calculating items quantity by counting all the items in the cart, since each item contain single product
	5. saving the items quanitity in the current session for future use
	"""

	try:
		cart_id = request.session["cart_id"]
		cart = Cart.objects.get(id=cart_id)
	except:
		cart = Cart.objects.create()
		cart.save()
		request.session["cart_id"] = cart.id

	product = Product.objects.get(slug=slug)
	try:
		qty = request.GET.get("qty")
	except:
		qty = None

	try:
		cart_item = Item.objects.get(product=product, cart=cart)

	except:
		cart_item = None

	if qty != '0' and not cart_item:
		Item.objects.create(product=product, cart=cart, quantity=qty)
	elif cart_item and qty == '0':
		cart_item.delete()
	else:
		cart_item.quantity = qty
		cart_item.save()

	cart.cart_total = 0.00
	for item in cart.item_set.all():
		item.item_total = float(item.product.sale_price) * item.quantity
		item.save()
		cart.cart_total += item.item_total
		cart.save()

	request.session["total_price"] = cart.cart_total
	request.session["total_items"] = cart.item_set.count()
	cart.save()
	return HttpResponseRedirect(reverse("cart"))
