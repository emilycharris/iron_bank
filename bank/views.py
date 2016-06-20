from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"

class ProfileView(ListView):
    model = Transaction
