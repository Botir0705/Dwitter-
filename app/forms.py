from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Dweet



class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	

class LogInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
       label="",
    )
    

    class Meta:
        model = Dweet
        fields = ['body']
	
    