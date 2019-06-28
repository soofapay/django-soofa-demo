from django.urls import path
from . import views


urlpatterns = [
    path('', views.PurchaseView.as_view()),
]