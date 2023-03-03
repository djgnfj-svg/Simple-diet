
from meals.Utils.Simul_manager import Nutrient_Buffer_Calculation

from managers.models import Diet_nutrient_manager


# 버퍼 확인용
class Diet_Manager(Nutrient_Buffer_Calculation):
    def __init__(self, validated_data) -> None:
        super().__init__(validated_data)
        if Diet_nutrient_manager.objects.count() == 0:
            self.protein_buffer = 1
            self.fat_buffer = 1
            self.carbohydrate_buffer = 1
            self.simul_buffer()
            # Diet_nutrient_manager.objects.create(
            #     protein_buffer = self.protein_buffer,
            #     fat_buffer = self.fat_buffer,
            #     carbohydrate_buffer = self.carbohydrate_buffer
            # )
        else:
            instance = Diet_nutrient_manager.objects.get(id=1)
            self.protein_buffer = instance.protein_buffer
            self.fat_buffer = instance.fat_buffer
            self.carbohydrate_buffer = instance.carbohydrate_buffer



# 출력용..?
class Diet_Meal_Calculation_Manager(Diet_Manager):
    def __init__(self, validated_data) -> None:
        Diet_Manager.__init__(self, validated_data)

    def get_diet_meal(self):
        return super().calc_meal(self.protein_buffer, self.fat_buffer, self.carbohydrate_buffer)