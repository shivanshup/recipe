from django.shortcuts import render
from veggie.models import recipe
from .forms import recipe
from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        

        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        
    queryset = recipe.objects.all()
    #search feature
    if request.GET.get('search'):
       queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
        
    context = {'recipes': queryset} 
    
    return render(request, 'recipes.html', context)

def update_recipe(request,id):
    queryset=recipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        queryset.save()
        return redirect('/recipes')
        
    context={'recipes':queryset} 
    
    return render (request,'recipe_update.html',context=context)

def delete_recipe(request, id):
    recipes = recipe.objects.get(id=id)
    print(recipes)         
    recipes.delete()                    
    return redirect('submit_recipe')       

def login_page(request):
    return render(request,'login.html')         

def register_page(request):
    return render(request,'register.html')                      