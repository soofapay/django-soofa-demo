import json
from ast import literal_eval
from decimal import Decimal

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django import forms
from django.shortcuts import render
from python_soofa import Soofa, Transaction

from demo.models import Payment

TILL_NUMBER = "5002"
SECRET_KEY = "3ixwt45uq88wttqgixpyla8d27ob0w"

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
     soofa = Soofa(TILL_NUMBER, SECRET_KEY)
     if soofa.find(tid):
        transaction: Transaction = soofa.get_transaction()
        if Decimal(amount) < transaction.gross_amount:
            return HttpResponseNotAllowed(f'Your payment of {transaction.receiver_currency}  {transaction.gross_amount} '
                                          f'is less than the expected {transaction.receiver_currency} '
                                          f'{amount}')
        print(transaction.tid)
        print(transaction.sender_currency)
        print(transaction.get_time())
        purchase = Payment.objects.create(data=transaction.json)
        return render(request, "home.html", {"payment": transaction, "purchase": purchase})

 return render(request, "home.html", {"payment": None, "purchase": None})

class PaymentView(TemplateView):
    template_name ="home.html"


@csrf_exempt
def webhook(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        transaction = Transaction(**data)
    except TypeError:
        return HttpResponseBadRequest("invalid data")

    print(transaction.get_time())
    print(transaction.tid)
    print(transaction.receiver_currency, transaction.gross_amount)
    print(transaction.json())
    purchase = Payment.objects.create(data=transaction.json())
    return HttpResponse("Accepted")
