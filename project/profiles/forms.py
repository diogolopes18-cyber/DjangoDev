from django import forms
from .models import UserForm
from datetime import datetime as dt

#Receives the parameters that we use on login
class UserLogin(forms.ModelForm):
    class Meta:
        model = UserForm
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = '__all__'
        date = dt.now()
class EntryVerification(forms.Form):
    date = dt.now()