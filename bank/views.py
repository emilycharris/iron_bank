from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank.models import Transaction
import datetime


# Create your views here.

def account_balance():
    balance = 0
    transactions = Transaction.objects.filter(user=self.request.user)
    for transaction in transactions:
        if transaction.transaction_type == 'Withdrawal':
            balance -= transaction.dollar_amount
        elif transaction.transaction_type == 'Deposit':
            balance += transaction.dollar_amount
    return balance, transactions


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
        filtered = Transaction.objects.filter(date__gte=datetime.datetime.now()-datetime.timedelta(days=30)).filter(user=self.request.user)
        context['filtered'] = filtered
        return context


class CreateTransactionView(CreateView):
    model = Transaction
    fields = ['vendor', 'dollar_amount', 'transaction_type' ]
    success_url = '/profile'

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        if transaction.transaction_type == 'DR':
            if transaction.dollar_amount > balance: #this is not correct
                raise Exception("You can't spend more than you have.")
            else:
                balance -= transaction.dollar_amount
        elif transaction.transaction_type == 'CR':
            balance += transaction.dollar_amount
        return super(CreateTransactionView, self).form_valid(form)

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
