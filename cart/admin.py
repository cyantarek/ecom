from django.contrib import admin

from cart.models import Cart, Item

class CartAdmin(admin.ModelAdmin):
	pass

admin.site.register(Cart, CartAdmin)
admin.site.register(Item)