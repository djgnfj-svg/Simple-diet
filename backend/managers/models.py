from django.db import models

from base.model_base.Time_model_base import TimeStampedModel

# Create your models here.

class diet_intake_manager(TimeStampedModel):
    pass


class diet_nutrient_manager(TimeStampedModel):
    portein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)
    portein_buffer = models.FloatField(default=0)