from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(req):
    return HttpResponse('<h1>Hello World!</h1>')