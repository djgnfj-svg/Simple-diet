from django.db import models
from django.utils.translation import gettext_lazy as _
import json

# Create your models here.

class Food_data(models.Model):
    class Nutrint(models.TextChoices):
        PROTEIN = 'P', _('단백질')
        FAT = 'F', _('지방')
        CARBOHYDRATE = 'C', _('탄수화물')

    # 분류
    nutrient_fucus = models.CharField(max_length=2,choices=Nutrint.choices,default=Nutrint.PROTEIN,)
    
    meals_fucus = models.JSONField()
    def set_meals_fucus(self, value):
        print("set_meals : ", value)
        self.meals_fucus = json.dumps(value)

    def get_meals_fucus(self):
        print("get_meals : ", self.meals_fucus)
        return json.loads(self.meals_fucus)
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