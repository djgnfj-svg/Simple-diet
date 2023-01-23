from django.db import models
from django.utils.translation import gettext_lazy as _
import json

# Create your models here.
class Meals_fucus(models.IntegerChoices):
    BREAKFAST = 0, '아침'
    LUNCH = 1, '점심'
    DINNER = 2, '저녁'


class Food_data(models.Model):
    class Nutrint(models.TextChoices):
        PROTEIN = 'P', _('단백질')
        FAT = 'F', _('지방')
        CARBOHYDRATE = 'C', _('탄수화물')

    # 분류
    nutrient_fucus = models.CharField(max_length=2,choices=Nutrint.choices,default=Nutrint.PROTEIN,)
    meals_fucus = models.IntegerField(default=Meals_fucus.BREAKFAST, choices=Meals_fucus.choices)
    
    # 정보
    name = models.CharField(max_length=50)
    kcalorie = models.IntegerField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    price = models.IntegerField()
    link = models.URLField(max_length=200)
    
    # 끼니
    food_number = models.IntegerField()
    food_gram = models.IntegerField()


    # def validate_meals_fucus(vlaue):
    #     return