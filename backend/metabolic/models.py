from django.db import models

from Simple_diet.Time_model_base import TimeStampedModel

# Create your models here.

# todo body_info_recode 가 필요하다 유저가 살을뺀것을 기록해주게
class Body_info(TimeStampedModel):
    age = models.IntegerField(null=False)
    weight = models.FloatField(null=False)
    height = models.FloatField(null=False)

    gender = models.CharField(null=False,max_length=2)
    general_activities = models.FloatField(null=False)
    excise_activity = models.FloatField(null=False)

    count = models.IntegerField(default=0)


class Metabolic(TimeStampedModel):
    total_kcalorie= models.FloatField(null=False)
    total_protein= models.FloatField(null=False)
    total_fat = models.FloatField(null=False)
    total_carbohydrate= models.FloatField(null=False)

    body_info = models.ForeignKey(Body_info, on_delete=models.SET_NULL, null=True)
    