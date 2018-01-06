from django.conf import settings
import stripe
from django.dispatch import receiver
from account.utils import hash_gen
from account.models import EmailConfirmed
from .models import UserStripe
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY

@receiver(user_logged_in)
def get_or_create_stripe(sender, user, *args, **kwargs):
	try:
		user.userstripe.stripe_id
	except UserStripe.DoesNotExist:
		customer = stripe.Customer.create(email=user.email)
		new_user_stripe = UserStripe.objects.create(user=user, stripe_id=customer.id)

@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
	if created:
		customer = stripe.Customer.create(email=instance.email)
		UserStripe.objects.create(user=instance, stripe_id=customer.id)
		email_confirmed, is_created = EmailConfirmed.objects.get_or_create(user=instance)
		if is_created:
			instance.emailconfirmed.key = hash_gen(instance.email)
			instance.emailconfirmed.save()
			email_confirmed.send_activation_email()

