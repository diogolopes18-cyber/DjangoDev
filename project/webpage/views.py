from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
#Imports the form
from profiles.forms import UserLogin
from profiles.models import UserForm
from profiles.forms import EntryVerification
from datetime import datetime as dt
import time
# Create your views here.

def home_page(request,*args,**kwargs):
    return render(request, "homepage.html",{})


def user_login(request):

    global current_date_time#Stores date and time of login

    # username = UserLogin.get(username=request.user.username)
    #Form Validation
    form1 = UserLogin(request.POST or None)
    if form1.is_valid():
        #instance = form1.save(commit=False)
        #instance.save()
        print("Ok")
        current_date_time = dt.now()
        print(current_date_time)
        return redirect("http://127.0.0.1:8000/admission/")


    #Context to be passed ot html page
    context = {
        "form": form1
    }
    return render(request, "login.html", context)#Returns page for login

    

def success_page(request,*args,**kwargs):
    return render(request,"success.html",{})#Returns page for successful login

def admission(request):
    #Form variables
    form2 = EntryVerification(request.POST)
    entry_button = request.POST['Entrada']
    exit_button = request.POST['Exit']
    date = dt.now()#gets current time

    #Request username from form
    username = request.user.username
    

    #Button verification
    if(request.method == 'POST'):
        form2 = EntryVerification(request.POST)
        if entry_button:
            redirect("http://127.0.0.1:8000/success/")#Redirects to success page
            #time.sleep(3)
            #redirect("http://127.0.0.1:8000/login/")
    
    #Passes arguments into html
    admission_context = {
        "form": form2,
        "date": date
    }

    return render(request,"admission.html",admission_context)

def credits(request):
    return render(request,"credits.html",{})