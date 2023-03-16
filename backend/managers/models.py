from django.db import models

from Simple_diet.Time_model_base import TimeStampedModel


# TODO : Ver0.9
# class Meal_Food_Options(TimeStampedModel):
#     # 연어 닭고기 등
#     protein_type_first = models.CharField(max_length=30, null=False) 
#     protein_type_second = models.CharField(max_length=30, null=True) 

#     # 견과류, 유제품 등
#     fat_type_first = models.CharField(max_length=30, null=False) 
#     fat_type_second = models.CharField(max_length=30, null=True) 
    
#     #밥 빵 등
#     carbohydrate_type_first = models.CharField(max_length=30, null=False) 
#     carbohydrate_type_second = models.CharField(max_length=30, null=True) 

#     # 간편식, 배달, 일반식, 직접하기 등등
#     etc_type_first = models.CharField(max_length=30, null=False)
#     etc_type_second = models.CharField(max_length=30, null=True) 

class Diet_nutrient_manager(TimeStampedModel):
    protein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)
    # custom_manager = models.ForeignKey(Meal_Food_Type, on_delete=models.CASCADE, null=True)