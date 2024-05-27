from django.shortcuts import render
from home.models import Car

# Create your views here.
# from django.http import HttpResponse
def home(request):
    
 return render(request,"home/index.html")
def about(request):
 context={'page':'About'}
 return render(request,"home/about.html",context)
 
def contact(request):
    
    
    
    return render(request,"home/contact.html")


