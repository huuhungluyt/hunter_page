from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login as auth_login

# Create your views here.
from .forms import SignupForm

def signup(request):
    if request.method=='POST':
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid():
            user=signup_form.save()
            auth_login(request, user)
            return redirect('techblog:index')
    else:
        signup_form= SignupForm()
    return render(request, "accounts/signup.html", {'signup_form': signup_form})