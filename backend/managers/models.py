from django.db import models

from Simple_diet.Time_model_base import TimeStampedModel

# Create your models here.
# 커스텀 매니져를 토대로 식단에 버퍼를 구한다.
# 버퍼가 삭제하면 커스텀 매니져 또한 삭제된다.
# 처음으로 들어오는 조합의 커스텀은 오래걸린다.
# 하지만 이미 있는 커스텀이라면 버퍼를 저장한 상태에서 진행하기 때문에 굉장히 빠르다.
 
class Meal_Food_Type(TimeStampedModel):
    # 연어 닭고기 등
    protein_type_first = models.CharField(max_length=30, null=False) 
    protein_type_second = models.CharField(max_length=30, null=True) 

    # 견과류, 유제품 등
    fat_type_first = models.CharField(max_length=30, null=False) 
    fat_type_second = models.CharField(max_length=30, null=True) 
    
    #밥 빵 등
    carbohydrate_type_first = models.CharField(max_length=30, null=False) 
    carbohydrate_type_second = models.CharField(max_length=30, null=True) 

    # 간편식, 배달, 일반식, 직접하기 등등
    etc_type_first = models.CharField(max_length=30, null=False)
    etc_type_second = models.CharField(max_length=30, null=True) 

class Diet_nutrient_manager(TimeStampedModel):
    protein_buffer = models.FloatField(default=0)
    fat_buffer = models.FloatField(default=0)
    carbohydrate_buffer = models.FloatField(default=0)
    custom_manager = models.ForeignKey(Meal_Food_Type, on_delete=models.CASCADE, null=True)