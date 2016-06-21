from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bank.models import Transaction


# Create your views here.

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
        balance = 0
        transactions = Transaction.objects.filter(user=self.request.user)
        for transaction in transactions:
            if transaction.transaction_type == 'DR':
                balance -= transaction.dollar_amount
            elif transaction.transaction_type == 'CR':
                balance += transaction.dollar_amount
        context['balance'] = balance
        context['transactions'] = transactions
        return context
