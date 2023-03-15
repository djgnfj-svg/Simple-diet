from django.db import models

from Simple_diet.Time_model_base import TimeStampedModel


class Food_Categories(TimeStampedModel):
    name = models.CharField(max_length=30, null=False, unique=True)
    

class Food(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    link = models.URLField(max_length=200)

    kcalorie = models.IntegerField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)

    food_number = models.IntegerField()
    food_gram = models.IntegerField()

    category = models.ManyToManyField(Food_Categories, null=True)
    