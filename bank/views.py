from django.shortcuts import render
from django.views.generic.base import TemplateView, CreateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CreateUser(CreateView):
