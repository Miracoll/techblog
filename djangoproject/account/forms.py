from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserRegistrationForm(UserCreationForm):
    last_name = forms.CharField()
    first_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['last_name','first_name','username','email','password1','password2']

class UpdateForm(forms.ModelForm):

    class Meta:
        models = User
        fields = ['last_name','first_name','email','bio','photo']