from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): #this custom form inherits from the UserCreationForm class of django
    email = forms.EmailField(required=True)

    class Meta:                           #this is a nested namespace for configurations and keeps the configurations in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): # this custom form inherits from the ModelForm class of django
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): # this custom form inherits from the ModelForm class of django

    class Meta:  
        model = Profile
        fields = ['image']