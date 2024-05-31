from django.shortcuts import render,redirect
from home.models import Car
from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
# Create your views here.
# from django.http import HttpResponse
@login_required
def home(request):
    
    return render(request,"home/index.html")
   
def about(request):
 context={'page':'About'}
 return render(request,"home/about.html",context)
 
def contact(request):
    
    
    
    return render(request,"home/contact.html")


