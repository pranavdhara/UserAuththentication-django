from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import RegistrationUserForm
# Create your views here.
@login_required
def index(request):

    return render(request,'userapp_authenicattion/index.html')


def signup(request):
    
    if request.method == "POST":
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account is created successfully!')
            return redirect('login')
    else:
        form = RegistrationUserForm()

    return render(request,'userapp_authenicattion/signup.html',{'form':form})



