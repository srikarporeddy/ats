from django.db import models
from django.conf import settings
# comment below line if we got error
from allauth.account.signals import user_logged_in, user_signed_up

import stripe
#from django.utils.datastructures import MultiValueDictKeyError

#secretKey = settings.STRIPE_SECRET_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.

class profile(models.Model):

	name = models.CharField(max_length=120)
	#comment user code if we got error
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	description = models.TextField(default = 'description default text')
	location = models.CharField(max_length=120, default = 'my location default', blank=True, null=True)
	#job = models.CharField(max_length=120, null=True)


	def __str__(self):
		return self.name
#comment below class if you got error
class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username

'''def my_callback(sender, request, user, **kwargs):
	idStripe, created = userStripe.objects.get_or_create(user=user)
	if created:
		print('created for %s'%(user.username))
	userProfile, is_created = profile.objects.get_or_create(user=user)
	if is_created:
		userProfile.name = user.username
		userProfile.save()
'''
def stripecallback(sender, request, user, **kwargs):
	user_stripe_account, created = userStripe.objects.get_or_create(user=user)
	if created:
		print('created for %s'%(user.username))
	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_account.stripe_id = new_stripe_id['id']
		user_stripe_account.save()
def profilecallback(sender, request, user, **kwargs):
	userProfile, is_created = profile.objects.get_or_create(user=user)
	if is_created:
		userProfile.name = user.username
		userProfile.save()

	
user_logged_in.connect(stripecallback)
user_signed_up.connect(profilecallback)
user_signed_up.connect(stripecallback)