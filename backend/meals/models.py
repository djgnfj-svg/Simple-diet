from django.db import models
# from managers.models import Meal_Food_Type

from foods.models import Food

from Simple_diet.Time_model_base import TimeStampedModel


# TODO : ver0.9 너무 크다 할것이 넘쳐흐른다.ㅋㅋㅋㅋ
# class Meals(TimeStampedModel):
#     편차_평균 = models.FloatField(null=True)
#     유져 = models.ForeignKey(user, on_delete=models.CASCADE)
    

class Meal(models.Model):
    meal_name = models.CharField(max_length=10)
    foods = models.ManyToManyField(Food, null=True)

    # meal_manager = models.ForeignKey(Meal_Food_Options)

    # meal_kcalorie = models.IntegerField(null=True)
    # meal_protien = models.IntegerField(null=True)
    # meal_fat = models.IntegerField(null=True)
    # meal_carbohydrate = models.IntegerField(null=True)

    # need_kcalorie = models.IntegerField(null=True)
    # need_protien = models.IntegerField(null=True)
    # need_fat = models.IntegerField(null=True)
    # need_carbohydrate = models.IntegerField(null=True)
    
    # meal_food_type = models.ForeignKey(Meal_Food_Type, on_delete=models.SET_NULL)
    # meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
