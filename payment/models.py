from django.db import models
from django.conf import settings

class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=120)

	def __str__(self):
		return self.stripe_id