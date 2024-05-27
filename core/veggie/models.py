from django.db import models

# Create your models here.
class recipe(models.Model):
    id=models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_image = models.ImageField(null=False, blank=False, upload_to="images/")
    recipe_description = models.TextField()
    
    
    def _str_(self) -> str:
        return self.recipe_name
    
    