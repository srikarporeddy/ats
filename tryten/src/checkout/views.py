from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
#from django.utils.datastructures import MultiValueDictKeyError

#secretKey = settings.STRIPE_SECRET_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		#print(request.POST)
		#token = request.POST
		token = request.POST#['stripeToken']
		
		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)
			charge = stripe.Charge.create(
			amount=1000,
			currency="usd",
  			customer=customer,
  			description="Example charge",
  			
		)
		except stripe.error.CardError:
			pass
		#print(token)
	

	context = {'publishKey':publishKey}
	template = 'checkout.html'
	return render(request,template,context)

