from django.db import models

# Create your models here.


class Account(models.Model):
    _total = models.DecimalField(max_digits=30, decimal_places=2)
    name = models.CharField(max_length=20)

    @classmethod
    def create(cls, total=0, name="Счет"):
        account = cls(_total = round(total, 2), name=name)
        account.save()
        return account

    def add_charge(self, charge):
        if self._total + charge.value < 0:
            return

        charge._account = self
        charge.save()
        self._total += charge.value

    @property
    def total(self):
        return self._total


class Charge(models.Model):
    _value = models.DecimalField(max_digits=10, decimal_places=2)
    _date = models.DateField()
    _account = models.ForeignKey("Account", related_name="charges")

    @property
    def value(self):
        return self._value

    @property
    def date(self):
        return self._date



