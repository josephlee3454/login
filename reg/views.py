from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import *


# Create your views here.
def index(request):
   
    return render(request, 'index.html')

def sucess(request):
   
    return render(request, 'sucess.html')
def regis(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value) 
            return redirect("/")
        else:
            user = User.objects.create(
                first_name = request.POST['first_name'], 
                last_name = request.POST['last_name'], 
                email = request.POST['email'], 
                password = request.POST['password'], 
                repassword=request.POST['repassword'])
            return redirect('/success')

