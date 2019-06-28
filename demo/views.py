from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.


class PurchaseView(TemplateView):
    template_name ="home.html"