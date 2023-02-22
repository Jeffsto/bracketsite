from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def login_user(request):
    if request.method == "POST":
        def my_view(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                # Return an 'invalid login' error message.
                messages.succes(request, (f'There was an issue logging in'))
                return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
