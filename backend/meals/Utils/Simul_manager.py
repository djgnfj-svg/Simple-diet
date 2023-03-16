import json

from meals.Utils.Meal_manager import Meal_Calculation


class Nutrient_Simuler():
    def __init__(self) -> None:
        self.nutrient_negative_value = 0.1
        self.simul_max_count = 5

        self.protein_buffer = 1
        self.fat_buffer = 1
        self.carbohydrate_buffer = 1
        self._simul_buffer()   
     
    def _simul_buffer(self):
        meal_list = ["breakfast", "lunch", "dinner"]
        simul_count = 0
        while simul_count < self.simul_max_count:
            _simul_protein_len, _simul_fat_len, _simul_carbohydrate_len = 1, 1, 1
            protein_buff_aver, fat_buff_aver, carbohydrate_buff_aver = 1, 1, 1

            with open('simul_data/diet_output.json') as f :
                simul_data = json.load(f)

            for data in simul_data.values():
                meal_calc = Meal_Calculation(data)
                meals_data = meal_calc.calc_meal(self.protein_buffer, self.fat_buffer, self.carbohydrate_buffer)
                need_data = meal_calc.meals
                for i in range(len(meals_data)):
                    meal = meals_data[meal_list[i]]["nutrient"]
                    need = need_data[meal_list[i]]

                    protein_gep = self._cal_diff_persent(meal["protein"], need["protein"])
                    protein_buff_aver = self._cal_aver(protein_buff_aver, protein_gep, _simul_protein_len)
                    _simul_protein_len += 1

                    fat_gep = self._cal_diff_persent(meal["fat"], need["fat"])
                    fat_buff_aver = self._cal_aver(fat_buff_aver, fat_gep, _simul_fat_len)
                    _simul_fat_len += 1

                    carbohydrate_gep = self._cal_diff_persent(meal["carbohydrate"], need["carbohydrate"])
                    carbohydrate_buff_aver = self._cal_aver(carbohydrate_buff_aver, carbohydrate_gep, _simul_carbohydrate_len)
                    _simul_carbohydrate_len += 1

            if self._check_buffer_twenty(protein_buff_aver):
                self.protein_buffer -= self.nutrient_negative_value
            if self._check_buffer_twenty(fat_buff_aver):
                self.fat_buffer -= self.nutrient_negative_value
            if self._check_buffer_twenty(carbohydrate_buff_aver):
                self.carbohydrate_buffer -= self.nutrient_negative_value
            simul_count += 1


    def _check_buffer_twenty(self, buff):
        if buff > 20:
            return True
        else :
            return False
    
    def _cal_diff_persent(self, a, b):
        return round((a-b) / b * 100)
    
    def _cal_aver(self, preAver, new_value, len):
        old_weight = (len - 1) / len
        new_weight = 1 / len
        return (preAver * old_weight) + (new_value * new_weight)
    
    def get_protein_buffer(self):
        return self.protein_buffer
    
    def get_fat_buffer(self):
        return self.fat_buffer
    
    def get_carbohydrate_buffer(self):
        return self.carbohydrate_buffer

