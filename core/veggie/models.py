from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recipe(models.Model):
    user=models.ForeignKey(User, on_delete = models.SET_NULL,null=True, blank=True)
    id=models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_image = models.ImageField(null=False, blank=False, upload_to="images/")
    recipe_description = models.TextField()
    
    
    def _str_(self) -> str:
        return self.recipe_name
    
    