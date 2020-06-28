from django.shortcuts import render

# Create your views here.

def user_details(request):
    return render(request,"timeline.html",{})