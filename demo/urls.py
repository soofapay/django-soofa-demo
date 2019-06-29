from django.urls import path
from . import views


urlpatterns = [
    path('', views.PurchaseView.as_view()),
    path("payment/", views.make_payment)
]