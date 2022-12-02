from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm  <-- django has a class to create a form for us, we just need to import it
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(response):
    if response.method == "POST":           #this is a post request, so we need to validate the form
        form = UserRegisterForm(response.POST)
        if form.is_valid():                 # if the form is valid, save the form and redirect to the home page
            form.save()                     #form.save() saves the user to the database (via registration page)
            username = form.cleaned_data.get('username')  
            messages.success(response, f'Account created for {username}! You can now log in!')
            return redirect('login')
        else:
            messages.error(response, f'Account could not be created!')

    else:
        form = UserRegisterForm()       #this is a get request, so we need to create a blank form
        
    return render(response, "users/register.html", {"form":form})


@login_required                 #this decorator ensures login before accessing the profile page (need to import it from django.contrib.auth.decorators)
def profile(response):
    if response.method == "POST":
        u_form = UserUpdateForm(response.POST, instance=response.user)  #this is the form for updating the user's username and email
        p_form = ProfileUpdateForm(response.POST,response.FILES,instance=response.user.profile)  #this is the form for updating the user's profile picture
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(response, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(response, f'Account could not be updated!')
    else:
        u_form = UserUpdateForm(instance=response.user)  #this is the form for updating the user's username and email
        p_form = ProfileUpdateForm(instance=response.user.profile)  #this is the form for updating the user's profile picture

    context = {
        'u_form': u_form,   
        'p_form': p_form	
    }
    return render(response, "users/profile.html", context=context)	