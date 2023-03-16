from meals.Utils.Meal_manager import Meal_Calculation
from managers.models import Diet_nutrient_manager

from meals.Utils.Simul_manager import Nutrient_Simuler


# 버퍼 확인용
class Diet_Manager():
    def __init__(self) -> None:
        if Diet_nutrient_manager.objects.count() == 0:
            simul_data = Nutrient_Simuler()
            self.protein_buffer = simul_data.protein_buffer
            self.fat_buffer = simul_data.fat_buffer
            self.carbohydrate_buffer = simul_data.carbohydrate_buffer

            Diet_nutrient_manager.objects.create(
                protein_buffer = simul_data.protein_buffer,
                fat_buffer = simul_data.fat_buffer,
                carbohydrate_buffer = simul_data.carbohydrate_buffer
            )
        else:
            instance = Diet_nutrient_manager.objects.first()
            self.protein_buffer = instance.protein_buffer
            self.fat_buffer = instance.fat_buffer
            self.carbohydrate_buffer = instance.carbohydrate_buffer


class Diet_Maker(Diet_Manager, Meal_Calculation):
    def __init__(self, validated_data) -> None:
        Diet_Manager.__init__(self)
        Meal_Calculation.__init__(self, validated_data)
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