from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
#Imports the form
from profiles.forms import UserLogin
from profiles.models import UserForm
from profiles.forms import EntryVerification
from datetime import datetime as dt
import time
import os
# Create your views here.

def home_page(request,*args,**kwargs):
    return render(request, "homepage.html",{})


def user_login(request):

    global current_date_time#Stores date and time of login

    # username = UserLogin.get(username=request.user.username)
    #Form Validation
    form1 = UserLogin(request.POST or None)
    if form1.is_valid():
        #form1.save()
        print("Ok")
        current_date_time = dt.now()
        return redirect("http://127.0.0.1:8000/admission/")


    #Context to be passed ot html page
    context = {
        "form": form1,
    }
    return render(request, "login.html", context)#Returns page for login

    

def success_page(request,*args,**kwargs):
    date = dt.now()#gets current time
    form2 = EntryVerification(request.POST)
    #username = UserLogin(request.POST)

    # if(request.path() == "http://127.0.0.1:8000/success/"):
    #     try:
    #         with open('time_file.txt','w') as time_file:
    #             time_file.write(str(date))#Writes distance into file
    #     except:
    #         print("Not able to write to file")

    date_context = {
        "form": form2,
        "date": date
    }


    return render(request,"success.html",date_context)#Returns page for successful login

def admission(request):
    #Form variables
    form2 = EntryVerification(request.POST)

    #Button verification
    if(request.method == 'POST'):
        form2 = EntryVerification(request.POST)
        if request.POST.get('exit') or request.POST.get('enter'):#Reads which button is pressed
            return redirect("http://127.0.0.1:8000/success/")#Redirects to success page
    
    #Passes arguments into html
    admission_context = {
        "form": form2
    }

    return render(request,"admission.html",admission_context)

def credits(request):
    return render(request,"credits.html",{})