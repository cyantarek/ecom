import datetime
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import EmailConfirmed


# Create your views here.

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")


def login_view(request):
	if request.method == "POST":
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		login(request, user)
		return redirect("/")
	template = "auth_templt/login_page.html"

	return render(request, template, {})


def register_view(request):
	if request.method == "POST":
		if request.POST["password"] != request.POST["password2"]:
			raise ValidationError("Password didn't match")
		user = User.objects.create(username=request.POST["username"], email=request.POST["email"])
		user.set_password(request.POST["password"])
		user.save()
		return redirect("login-view")
	template = "auth_templt/signup_page.html"

	return render(request, template, {})


def activation_view(request, activation_key):
	try:
		email_conf = EmailConfirmed.objects.get(key=activation_key)
		time_diff = datetime.datetime.now(datetime.timezone.utc) - email_conf.timestamp
	except:
		time_diff = None
		email_conf = None


	if email_conf and not email_conf.confirmed and time_diff < datetime.timedelta(hours=24):
		email_conf.confirmed = True
		email_conf.save()
		context = {
			"status": "activated",
		}
	elif email_conf and email_conf.confirmed:
		context = {
			"status": "already_activated",
		}
	elif email_conf and time_diff > datetime.timedelta(minutes=1):
		email_conf.delete()
		context = {
			"status": "expired",
		}
	else:
		template = "product/404.html"
		return render(request, template, {})
	template = "auth_templt/activated.html"
	return render(request, template, context)
