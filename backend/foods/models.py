from django.db import models

# Create your models here.
class Meals_fucus(models.IntegerChoices):
    BREAKFAST = 0, 'Low'
    LUNCH = 1, 'Normal'
    DINNER = 2, 'High'

class Food_data(models.Model):
    nutrient_fucus = models.CharField(max_length=10)
    meals_fucus = models.IntegerField(default=Meals_fucus.BREAKFAST, choices=Meals_fucus.choices)
    name = models.CharField(max_length=50)
    kcalorie = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    price = models.IntegerField()
    food_number = models.IntegerField()
    food_gram = models.IntegerField()
    link = models.URLField(max_length=200)