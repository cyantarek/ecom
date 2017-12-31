from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
	fields = [
	]
	readonly_fields = [
		"order_id",
		"timestamp",
		"updated",
	]

admin.site.register(Order)