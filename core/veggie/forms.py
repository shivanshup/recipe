from django import forms
from .models import recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['recipe_name', 'recipe_image', 'recipe_description']
