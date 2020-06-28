from django import forms
from .models import UserForm
from datetime import datetime as dt

#Receives the parameters that we use on login
class UserLogin(forms.Form):
    class Meta:
        model = UserForm
        fields = [
            'title'
        ]
    username = forms.CharField(label="username", max_length=30, min_length=5)
    password = forms.CharField(label="password", max_length=30,widget=forms.PasswordInput)
    #current_date = dt.now()

class EntryVerification(forms.Form):
    date = dt.now()