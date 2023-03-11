from django.db import models

from base.model_base.Time_model_base import TimeStampedModel


# todo : 선호를 표시할 수 있는 지표
class Food_Categories(TimeStampedModel):
    name = models.CharField(max_length=30, null=False, unique=True)
    

class Food(TimeStampedModel):
    # 기본 정보
    name = models.CharField(max_length=50, unique=True)
    link = models.URLField(max_length=200)
    category = models.ForeignKey(Food_Categories, on_delete=models.CASCADE, null=True, related_name='category')
    meals_fucus = models.JSONField() # 구지 아침점심저녁을 나누어야하나?

    # 영양소 정보
    kcalorie = models.IntegerField(default=0)
    protein = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)

    # 끼니별 정보
    food_number = models.IntegerField()
    food_gram = models.IntegerField()
    