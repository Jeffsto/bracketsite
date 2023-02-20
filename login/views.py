from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'authenticate/login.html', {})

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
