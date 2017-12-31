from django.contrib import admin
from .models import Product, ProductImage

# Register your models here.

class InlineProductImage(admin.StackedInline):
	model = ProductImage
	extra = 1


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = "timestamp"
	list_display = [
		"title",
		"price",
		"updated",
		"active",
	]
	search_fields = [
		"title",
	]
	list_editable = [
		"price",
		"active",
	]
	list_filter = [
		"price",
		"active",
	]
	readonly_fields = [
		"updated",
		"timestamp",
	]
	prepopulated_fields = {
		"slug": ("title",)
	}
	inlines = [
		InlineProductImage
	]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)