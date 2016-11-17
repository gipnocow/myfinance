from django import forms
from .models import Charge, Account


class ChargeForm(forms.ModelForm):
    _value = forms.DecimalField(label = 'Сумма', required = True)
    _date = forms.DateField(label = 'Дата', required = True)

    class Meta:
        model = Charge
        fields = ("_value", "_date")


class AccountForm(forms.ModelForm):
    _total = forms.DecimalField(label = 'Сумма', required = True)
    name = forms.CharField(label="Имя счета", max_length=20)

    class Meta:
        model = Account
        fields = ("_total", "name")