from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myusers = Member.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers':myusers,
    }
    return HttpResponse(template.render(context,request))
