import json

from meals.Utils.Meal_manager import Meal_Calculation


class Nutrient_Buffer_Calculation(Meal_Calculation):
    def __init__(self, total_data) -> None:
        super().__init__(total_data)
        self._simul_protein_len = 1
        self._simul_fat_len = 1
        self._simul_carbohydrate_len = 1
    def simul_buffer(self):
        '''
        버퍼를 조금식올리면서 5%이하이면 통과시키기
        '''
        protein_buff_aver = 100
        fat_buff_aver = 100
        carbohydrate_buff_aver = 100
    
        meal_list = ["breakfast", "lunch", "dinner"]
        # todo : 파일이 없을때 사용할 로직 만들기
        # list out of range가 나오면 여기를 의심해야됨
        while (protein_buff_aver > 20 or fat_buff_aver > 20 or carbohydrate_buff_aver > 20):
            # self._simul_protein_len = 1
            # self._simul_fat_len = 1
            # self._simul_carbohydrate_len = 1
            protein_buff_aver = 1
            fat_buff_aver = 1
            carbohydrate_buff_aver = 1

            # todo 없다면 base파일을 실행하는 거시가
            with open('base/simul_data/diet_output.json') as f :
                simul_data = json.load(f)

            for data in simul_data.values():
                test_data = Meal_Calculation(data)
                meals_data = test_data.calc_meal(self.protein_buffer, self.fat_buffer, self.carbohydrate_buffer)
                need_data = test_data.meals
                for i in range(len(meals_data)):
                    meal = meals_data[meal_list[i]]["nutrient"]
                    need = need_data[meal_list[i]]

                    protein_gep = self._cal_diff_persent(meal["protein"], need["protein"])
                    protein_buff_aver = self._cal_aver(protein_buff_aver, protein_gep, self._simul_protein_len)
                    self._simul_protein_len += 1

                    fat_gep = self._cal_diff_persent(meal["fat"], need["fat"])
                    fat_buff_aver = self._cal_aver(fat_buff_aver, fat_gep, self._simul_fat_len)
                    self._simul_fat_len += 1

                    carbohydrate_gep = self._cal_diff_persent(meal["carbohydrate"], need["carbohydrate"])
                    carbohydrate_buff_aver = self._cal_aver(carbohydrate_buff_aver, carbohydrate_gep, self._simul_carbohydrate_len)
                    self._simul_carbohydrate_len += 1

            # todo : 만약 이전값과 똑같아면 계산안의 로직을 교체하지 않는이상 무리이다.
            if self._check_buffer_20up(protein_buff_aver):
                self.protein_buffer -= 0.1
            if self._check_buffer_20up(fat_buff_aver):
                self.fat_buffer -= 0.1
            if self._check_buffer_20up(carbohydrate_buff_aver):
                self.carbohydrate_buffer -= 0.1
            f.close()
    


    def _check_buffer_20up(self, buff):
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
