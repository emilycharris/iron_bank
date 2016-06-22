from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank.models import Transaction
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.http import request, HttpResponse
from django.contrib import messages






# Create your views here.

def account_balance(self):
    self.balance = 0
    transactions = Transaction.objects.filter(user=self.request.user)
    for transaction in transactions:
        if transaction.transaction_type == 'Withdrawal':
            self.balance -= transaction.dollar_amount
        elif transaction.transaction_type == 'Deposit':
            self.balance += transaction.dollar_amount
    return self.balance



class IndexView(TemplateView):
    template_name = 'index.html'

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"

class ProfileView(ListView):
    model = Transaction

    def get_context_data(self):
        context = super().get_context_data()
        balance = account_balance(self)
        filtered = Transaction.objects.filter(date__gte=datetime.datetime.now()-datetime.timedelta(days=30), user=self.request.user)
        context['filtered'] = filtered
        context['balance'] = balance
        return context


class CreateTransactionView(CreateView):
    model = Transaction
    fields = ['vendor', 'dollar_amount', 'transaction_type' ]
    success_url = '/profile'

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        balance = account_balance(self)
        if transaction.dollar_amount > balance:
            return HttpResponse("You can't spend more than you have.")
        else:
            return super(CreateTransactionView, self).form_valid(form)

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class CreateTransferView(CreateView):
    model = Transaction
    fields = ['vendor', 'dollar_amount' ]
    success_url = '/profile'

    def form_valid(self, form):
        transfer = form.save(commit=False)
        transfer.user = self.request.user
        balance = account_balance(self)
        if transfer.dollar_amount > balance:
            return HttpResponse("You can't transfer more than you have.")
        else:
            transfer_to = User.objects.get(id=transfer.vendor)
            Transaction.objects.create(user=transfer_to, dollar_amount=transfer.dollar_amount,
                vendor="", transaction_type='Deposit' )

        return super(CreateTransferView, self).form_valid(form)
