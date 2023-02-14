from django.db import models
from django.utils.translation import gettext_lazy as _
import json

# Create your models here.

# todo : 선호를 표시할 수 있는 지표
class Food_Categories(models.Model):
    name = models.CharField(max_length=30, null=False)
    
    # todo : 통합 클래스로 빼고 상속받는 형태로 만든다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Food_data(models.Model):
    class Nutrint(models.TextChoices):
        PROTEIN = 'P', _('단백질')
        FAT = 'F', _('지방')
        CARBOHYDRATE = 'C', _('탄수화물')

    # 분류
    nutrient_fucus = models.CharField(max_length=2,choices=Nutrint.choices,default=Nutrint.PROTEIN,)
    meals_fucus = models.JSONField()
    
    # 정보
    name = models.CharField(max_length=50, unique=True)
    kcalorie = models.IntegerField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    price = models.IntegerField()
    link = models.URLField(max_length=200)
    category = models.ForeignKey(Food_Categories, on_delete=models.CASCADE, null=True)
    # 끼니
    food_number = models.IntegerField()
    food_gram = models.IntegerField()

    # 추후 통합 클래스로 뺴고 상속받자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)