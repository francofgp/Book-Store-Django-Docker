from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
from django.contrib.auth.models import Permission

stripe.api_key = "sk_test_51IIHlSJmLbh1Z5Ju87YZw6a4OokqKzPQrwkjrjeEiwxaaaP3Nx7vKPF6P48liV0UCE7le9NWZQ63HvOqkHF1o7Nn00NAX2stUG"
# stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = "pk_test_51IIHlSJmLbh1Z5JudJvlF1WQegzeGWzLb1JlTDsf12tkEs4X7pLoo8s1gJqBsqQguQBm3LK2hIIU7sBCymTXMdpQ00Ff6gYRTp"

        # context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):  # new
    # Get the permission
    permission = Permission.objects.get(codename='special_status')

    # Get user
    u = request.user

    # Add to user's permission set
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')
