from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Users
def index(request):
    return HttpResponse("Hi!, Welcome to my learning project")
# Create your views here.

def listofusers(request):
    x = Users.objects.all()
    objects = []
    for i in x:
        objects.append(i.get_datalist())
    template = loader.get_template('polls/users.html')
    context = {
        'userlist' : objects
    }
    print(objects)
    return HttpResponse(template.render(context,request))