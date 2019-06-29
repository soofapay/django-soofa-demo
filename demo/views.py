from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django import forms
from django.shortcuts import render


class PaymentForm(forms.Form):
   tid = forms.CharField(max_length=20)
   reference = forms.CharField(max_length=150)
   amount = forms.FloatField()

def make_payment(request):
 if request.method == 'POST':
   payment_form = PaymentForm(request.POST)
   if payment_form.is_valid():
     tid = payment_form.cleaned_data.get("tid")
     reference = payment_form.cleaned_data.get("reference")
     amount = payment_form.cleaned_data.get("amount")
     print("Amount : ", amount)
     print("tid : ", tid)
     print("reference : ", reference)
     return render(request, "home.html", {"payment_information": "jsjsj"})

 return render(request, "home.html", {"payment_information": "jsjsj"})

class PurchaseView(TemplateView):
    template_name ="home.html"

