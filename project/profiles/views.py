from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_page(*args,**kwargs):
    return HttpResponse("<h1>Welcome to the Login page</h1>")