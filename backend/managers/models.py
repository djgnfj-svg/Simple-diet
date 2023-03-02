from django.db import models

from base.model_base.Time_model_base import TimeStampedModel

# Create your models here.
 
class Diet_custom_manager(TimeStampedModel):
    pass

class Diet_nutrient_manager(TimeStampedModel):
    protein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)

    # todo : 식단 커스텀 페이지를 만들떄 추가예정
    # protein_option = models.JSONField()
    # fat_option = models.JSONField()
    # carbohydrate_option = models.JSONField()