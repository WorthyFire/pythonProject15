from django.contrib.auth.views import LoginView
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

class LoginView(LoginView):
    template_name = 'main/login.html'

def ViewAbout(request):
    return render(request, 'main/about.html')
