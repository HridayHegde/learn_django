from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Users
from django.urls import reverse

from django.http import Http404
def index(request):
    return HttpResponse("Hi!, Welcome to my learning project")
# Create your views here.

def listofusers(request):
    try:
        x = Users.objects.all()
    except Users.DoesNotExist:
        raise Http404("Users Do not exist")
    objects = []
    for i in x:
        objects.append(i.get_datalist())
    context = {
        'userlist' : objects
    }
    print(objects)
    return render(request, 'polls/users.html', context)

def add_user(request):
    username = request.POST['uname']
    password = request.POST['pass']
    user = Users(username = username,password = password)
    try:
        x = Users.objects.all()
    except Users.DoesNotExist:
        raise Http404("Users Do not exist")
    objects = []
    for i in x:
        objects.append(i.get_datalist())
    try:
        user.save()
    except OSError as e:
        return render(request,'polls/form.html',{'error_message' : "Database Faliure",'userlist': objects})
    return HttpResponseRedirect(reverse('polls:users'))
def show_form(request):
    try:
        x = Users.objects.all()
    except Users.DoesNotExist:
        raise Http404("Users Do not exist")
    objects = []
    for i in x:
        objects.append(i.get_datalist())
    context = {
        'userlist' : x
    }
    print(objects)
    return render(request, 'polls/form.html', context)