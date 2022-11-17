from django.contrib import admin
from django.urls import path

from payment.views import (CancelView, CreateCheckoutSessionView,
                           ItemLandingPageView, SuccessView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),
    path('item/<int:pk>/', ItemLandingPageView.as_view(), name='item-page'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
