from django.shortcuts import render
from veggie.models import recipe
from .forms import recipe
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def recipes(request):
    user=get_user(request)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        
        if isinstance(user,AnonymousUser):
            return redirect("/recipes")
        else:     

            recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
            user_id=user.id
        )
        
    queryset = recipe.objects.all()
    #search feature
    if request.GET.get('search'):
       queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
        
    context = {'recipes': queryset,'user':user.id} 
    
    return render(request, 'recipes.html', context)

def update_recipe(request,id):
    queryset=recipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        # recipe_image = request.FILES.get("recipe_image")
        
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        
        queryset.save()
        return redirect('/recipes')
        
    context={'recipes':queryset} 
    user=get_user(request)
    if queryset.user_id==user.id:  
        return render (request,'recipe_update.html',context=context)     
        
    else:                  
        return redirect('submit_recipe')     
    # return render (request,'recipe_update.html',context=context)

def delete_recipe(request, id):
    recipes = recipe.objects.get(id=id)
    print(recipes)
    user=get_user(request)
    if recipes.user_id==user.id:       
        recipes.delete() 
    else:                  
        return redirect('submit_recipe')       
from django.contrib.auth import get_user,logout
from django.contrib.auth.models import AnonymousUser
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        from django.contrib.auth import authenticate,login
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user=user)
        else:
            return render(request,'login.html',context={
                "error":"Invalid user"
            })
        
        # print(user.username)
        print(request.POST.get('next'))
        next_url=request.POST.get('next')
        if next_url==None:
            print("============")
            print(request.POST.get('next'))
            return redirect("/")
        else:
            print("hairy pussy")
            return redirect(next_url)
    elif request.method=="GET":
        next=request.GET.get('next')
        if next==None:
            next='/'
        user=get_user(request)
        if isinstance(user,AnonymousUser):
            return render(request,'login.html',context={
                'next':next
            })  
        else:
            # logout(request)
            return redirect("/recipes")
        
    
    
    
    return render(request,'login.html')         

def register_page(request):
   if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(email,username,password)
        
        user = User.objects.create(
            email=email,
            username=username
        )
        
        user.set_password(password)
        user.save()
        
        return redirect("/login")
   else:
       return render(request, 'register.html')
        
        
@login_required
def logout_view(request):
    
    logout(request)
    return redirect("/")

    
    
                        