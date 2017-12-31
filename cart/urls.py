from django.conf.urls.static import static
from django.urls import path
from ecommerce1 import settings
from . import views

urlpatterns = [
	path("", views.view, name="cart"),
	path("<slug>/", views.update_cart, name="update-cart"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)