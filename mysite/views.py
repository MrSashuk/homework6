from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Phone

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class UserListView(ListView):
    model = Phone
    template_name = 'users.html'
    context_object_name = 'phone_list'



