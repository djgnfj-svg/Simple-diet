from django.db import models
from django.utils.translation import gettext_lazy as _


# todo : 선호를 표시할 수 있는 지표
class Food_Categories(models.Model):
    name = models.CharField(max_length=30, null=False)
    
    # todo : 통합 클래스로 빼고 상속받는 형태로 만든다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Food_data(models.Model):
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
    
    # 추후 통합 클래스로 뺴고 상속받자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)