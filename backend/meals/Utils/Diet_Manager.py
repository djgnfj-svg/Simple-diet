from managers.models import Diet_nutrient_manager

from meals.Utils.Simul_manager import Nutrient_Buffer_Calculation


# 버퍼 확인용
class Diet_Manager(Nutrient_Buffer_Calculation):
    def __init__(self, validated_data) -> None:
        super().__init__(validated_data)
        if Diet_nutrient_manager.objects.count() == 0:
            self.protein_buffer = 1
            self.fat_buffer = 1
            self.carbohydrate_buffer = 1
            self.simul_buffer()
            Diet_nutrient_manager.objects.create(
                protein_buffer = self.protein_buffer,
                fat_buffer = self.fat_buffer,
                carbohydrate_buffer = self.carbohydrate_buffer
            )
        else:
            instance = Diet_nutrient_manager.objects.first()
            self.protein_buffer = instance.protein_buffer
            self.fat_buffer = instance.fat_buffer
            self.carbohydrate_buffer = instance.carbohydrate_buffer


import json

class Diet_Maker(Diet_Manager):
    def __init__(self, validated_data) -> None:
        Diet_Manager.__init__(self, validated_data)
        self.diet = self.calc_meal(self.protein_buffer, self.fat_buffer, self.carbohydrate_buffer)
    def get_diet(self):
        return self.diet
    
    def get_meal_foods(self, meal_name):
        rtn = []
        #식사 수만큼 반복함
        for test in self.diet[meal_name]:
            if test == "nutrient":
                break
            rtn.append(self.diet[meal_name][test]["food_name"])
        return rtn