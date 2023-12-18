from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import CreateProductForm


def index(request):
    return render(request, 'main/index.html')

class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('main:create_service')

def viewabout(request):
    return render(request, 'main/about.html')

def viewcontacts(request):
    return render(request, 'main/contacts.html')

class ProductList(ListView):
    model = Product
    template_name = 'main/service.html'
    context_object_name = 'products'

class CreateProduct(CreateView):
    model = Product
    template_name = 'main/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('main:service')