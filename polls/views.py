from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi!, Welcome to my learning project")
# Create your views here.
