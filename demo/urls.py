from django.urls import path
from . import views


urlpatterns = [
    path('', views.PaymentView.as_view()),
    path("payment/", views.make_payment),
    path("webhook/", views.webhook)
]
