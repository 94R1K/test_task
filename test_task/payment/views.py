import os

import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic.base import TemplateView
from dotenv import load_dotenv

from .models import Item

load_dotenv()
stripe.api_key = os.getenv('STRIPE_SECRET_API_KEY')


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemLandingPageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": os.getenv('STRIPE_PUBLIC_API_KEY')
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
