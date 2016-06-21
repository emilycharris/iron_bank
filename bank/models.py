from django.db import models
from django.contrib.auth.models import User




# Create your models here.

transaction_type = ['deposit', 'withdrawal']

class Transaction(models.Model):

    DEBIT = 'Withdrawal'
    CREDIT = 'Deposit'
    TRANSACTION_CHOICES = (
        (DEBIT, 'Withdrawal'),
        (CREDIT, 'Deposit'),
    )
    user = models.ForeignKey(User)
    dollar_amount = models.DecimalField(max_digits=100,decimal_places=2)
    vendor = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES, default=DEBIT)

    class Meta:
        ordering = ['-date']
