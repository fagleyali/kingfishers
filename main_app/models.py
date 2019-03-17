from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

Meals=(
    ('IN','Insects'),
    ('FR', 'Frogs'),
    ('FI', 'Fish')
)

class Location(models.Model):
    where=models.CharField(max_length=50)
    

    def __str__(self):
        return self.where
    
    def get_absolute_url(self):
        return reverse('locations_detail',kwargs={'pk':self.id})

# Create your models here.

class Kingfisher(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age=models.IntegerField()
    location=models.ManyToManyField(Location)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'kingfisher_id':self.id})
    
class Feeding(models.Model):
    date=models.DateField('feeding date')
    meal=models.CharField(
        max_length=2,
        choices=Meals,
        default=Meals[0][0]
        
    )
    kingfisher = models.ForeignKey(Kingfisher, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
        

        

