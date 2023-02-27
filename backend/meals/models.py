from django.db import models
from foods.models import Food

from base.model_base.Time_model_base import TimeStampedModel



class Meals_Custom(models.Model):
    protein_option = models.IntegerField(null=True)
    fat_option = models.IntegerField(null=True)
    carbohydrate_option = models.IntegerField(null=True)

    diet_status = models.FloatField(null=False)
    many_meals = models.IntegerField(null=False)

class Meal(models.Model):
    foods = models.ManyToManyField(Food, on_delete=models.DO_NOTHING, null=True)
    meal_custom = models.ForeignKey(Meals_Custom, on_delete=models.SET_NULL, null=True)
    protien = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    carbohydrate = models.IntegerField(null=True)
    pass

class Meals(TimeStampedModel):
    meal_list = models.ForeignKey(Meal, on_delete=models.CASCADE)
    pass