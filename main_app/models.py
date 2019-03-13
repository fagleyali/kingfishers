from django.db import models
from django.urls import reverse

Meals=(
    ('IN','Insects'),
    ('FR', 'Frogs'),
    ('FI', 'Fish')
)

# Create your models here.

class Kingfisher(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age=models.IntegerField()

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
    
        

        

