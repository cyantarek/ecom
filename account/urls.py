from django.urls import path

from account import views

urlpatterns = [
	path("logout/", views.logout_view, name="logout-view"),
	path("login/", views.login_view, name="login-view"),
	path("signup/", views.register_view, name="signup-view"),
	path("activate/<activation_key>/", views.activation_view, name="activation-view"),
]