from django.shortcuts import render
from datetime import date
from decimal import Decimal
from .models import Account, Charge
from random import randint
from .forms import ChargeForm, AccountForm


def accounts_page(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
    else:
        form=AccountForm()
    return render(request,
                  'finance/accounts_page.html',
                  {'accounts':Account.objects.all(), 'form':form})


def account_details_page(request, pk):
    account = Account.objects.get(pk=pk)
    if request.method == "POST":
        form = ChargeForm(request.POST)
        if form.is_valid():
            charge = form.save(commit=False)
            account.add_charge(charge)
            account.save()

    else:
        form = ChargeForm()

    return render(request, 'finance/account_details_page.html', {"account": account, "form":form})




