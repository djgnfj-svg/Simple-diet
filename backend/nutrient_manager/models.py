from django.db import models

# Create your models here.


class Nutrient_manager(models.Model):
    protein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)

    food_number = models.IntegerField(null=True) # 음식의 총 갯수를 알아야 할지 모른다?

    # def create(self, *args, **kwargs):

    #     super().save(*args, **kwargs)

    def create(self, **kwargs):
        print("들어오기는함")
        pass