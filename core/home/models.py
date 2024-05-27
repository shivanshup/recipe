from django.db import models

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField()
    Address= models.TextField()
    Image= models.ImageField()
    File= models.FileField()
    
class Car(models.Model):
    id=models.IntegerField(primary_key=True)
    car_name=models.CharField(max_length=100)  
    speed=models.IntegerField(null = True)  
    def __str__(self):
        return self.car_name
  
