from django import forms
from .models import UserForm
from datetime import datetime as dt

#Receives the parameters that we use on login
class UserLogin(forms.Form):
    class Meta:
        model = UserForm
        widgets = {
            'password': forms.PasswordInput()
        }

class EntryVerification(forms.Form):
    date = dt.now()