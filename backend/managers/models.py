from django.db import models

from Simple_diet.Time_model_base import TimeStampedModel

# Create your models here.
 
 
class Diet_custom_manager(TimeStampedModel):
    pass


class Diet_nutrient_manager(TimeStampedModel):
    protein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)