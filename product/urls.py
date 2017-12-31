from django.conf.urls.static import static
from django.urls import path
from ecommerce1 import settings
from . import views

urlpatterns = [
	path("s/", views.product_search, name="search"),
	path("<slug>/", views.product_detail, name="detail"),
	path("", views.index, name="home"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)