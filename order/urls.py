from django.conf.urls.static import static
from django.urls import path
from ecommerce1 import settings
from . import views

urlpatterns = [
	path("checkout/", views.checkout, name="checkout")
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)