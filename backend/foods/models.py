from django.db import models

# Create your models here.

class Food_data(models.Model):
    fucus = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    kcalorie = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    price = models.IntegerField()
    food_number = models.IntegerField()
    food_gram = models.IntegerField()
    link = models.URLField(max_length=200)