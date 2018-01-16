from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.core.mail import send_mail
from ecommerce1 import settings

User = get_user_model()


class EmailConfirmed(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	key = models.CharField(max_length=120)
	confirmed = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)

	def avtivate_user(self):
		pass
	def send_activation_email(self):
		activation_url = "http://127.0.0.1:8000/accounts/activate/%s" % self.key
		subject = "Activate your account"
		message = """
		Hello {},
		Please activate your account by following this link: {}
		Thank you
		""".format(self.user.username, activation_url)
		from_email = settings.DEFAULT_FROM_EMAIL
		send_mail(subject, message, from_email, [self.user.email])

	def __str__(self):
		return self.user.email + " - " + str(self.confirmed)
