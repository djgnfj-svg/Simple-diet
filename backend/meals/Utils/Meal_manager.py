from meals.Utils.Diet_Calcuation import Metabolic_Calculator
from metabolic_calculator.models import Body_info

from meals.Utils.Food_Manager import Food_Manager

from foods.models import Food

import json

#식단 나누기 용도
class Meals_Separation_Manager:
    def __init__(self, total_data) -> None:
        self.total_data = total_data
        
        self._diet_cut = 0.8 if total_data["diet_status"] else 1
        self._init_total_data()

        if total_data["meal_count"] == 3:
            self._meal_ratio = [0.25, 0.45, 0.3]
            self._meal_list = ["breakfast", "lunch", "dinner"]
        elif total_data["meal_count"] == 2:
            self._meal_ratio = [0.6, 0.4]
            self._meal_list = ["breakfast", "lunch"]
        else:
            self._meal_ratio = [1]
            self._meal_list = ["breakfast"]

        self.meals = {}
        self._cal_meals_ratio()

    def _init_total_data(self):
        self.total_kcalorie = self.total_data["total_kcalorie"] * self._diet_cut
        self.total_protein = self.total_data["total_protein"] * self._diet_cut
        self.total_fat = self.total_data["total_fat"] * self._diet_cut
        self.total_carbohydrate = self.total_data["total_carbohydrate"] * self._diet_cut

    def _cal_meals_ratio(self):
        for i, meal in enumerate(self._meal_list):
            self.meals[meal] = {}
            self.meals[meal]["kcalorie"] = round(self.total_kcalorie * self._meal_ratio[i])
            self.meals[meal]["protein"] = round(self.total_protein * self._meal_ratio[i])
            self.meals[meal]["fat"] = round(self.total_fat * self._meal_ratio[i])
            self.meals[meal]["carbohydrate"] = round(self.total_carbohydrate * self._meal_ratio[i])

    def get_meals(self):
        return self.meals
    

#식단 계산용
class Meal_Calculation(Meals_Separation_Manager, Food_Manager):
    def __init__(self, total_data) -> None:
        Meals_Separation_Manager.__init__(self,total_data)
        Food_Manager.__init__(self)
        #todo 추후 깔끔하게
        if total_data["meal_count"] == 3:
            self.breakfast = self.meals["breakfast"]
            self.lunch = self.meals["lunch"]
            self.dinner = self.meals["dinner"]
        elif total_data["meal_count"] == 2:
            self.breakfast = self.meals["breakfast"]
            self.lunch = self.meals["lunch"]
        else:
            self.breakfast = self.meals["breakfast"]
            
    # todo : 함수 구조 변경
    def _add_meal_food_data(self, meal_food_data, meal_nutrient_data, food: Food,
                            meal, food_count, food_double):
        double_value = 2 if food_double else 1
        big_size = 1
        food_number = 1
        if food.food_gram > 500:
            self._meal_have_bigsize_food = True
            if food.food_gram > 800:
                big_size = 3
                food_number = 0.3
            else:
                big_size = 2
                food_number = 0.5

        meal_food_data[str(food_count)] = self._set_meal_food_data(food, big_size, food_number, double_value)
        self._set_meal_nutrient_data(meal_nutrient_data[meal], food, big_size, double_value)


    def calc_meal(self,protein_buff=1, fat_buff=1, carbohydrate_buff=1):
        diet_info = {}
        for _, meal in enumerate(self._meal_list):
            meal_food_data = {}
            self._protein_full = False
            self._fat_full = False
            self._carbohydrate_full = False
            self._meal_have_bigsize_food = False
            
            meal_nutrient_data = {}
            meal_nutrient_data[meal] =  self._init_nutrient_data()

            food_count = 0
            food_focus = 0
            while not self._carbohydrate_full:
                food = self._get_food(meal, food_focus)

                if (food.food_gram > 500 and self._meal_have_bigsize_food) or \
                    self._check_food_over_nutrient(food, meal, meal_nutrient_data):
                    food_focus += 1
                    continue
    
                food_double = self._check_food_double(food, meal, meal_nutrient_data)
                meal_food_data[str(food_count)] = self._init_nutrient_data()
                self._add_meal_food_data(meal_food_data, meal_nutrient_data, food, meal, food_count, food_double)
                food_count += 1
                food_focus = self._check_nutrient(meal, meal_nutrient_data, food_focus,
                                protein_buff, fat_buff, carbohydrate_buff)

            diet_info[meal] = meal_food_data
            diet_info[meal]["nutrient"] = meal_nutrient_data[meal]
        return diet_info

# todo : 버퍼 계산용
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
        protein_buff = 1
        fat_buff = 1
        carbohydrate_buff = 1

        protein_buff_aver = 100
        fat_buff_aver = 100
        carbohydrate_buff_aver = 100
    
        meal_list = ["breakfast", "lunch", "dinner"]
        # todo : 파일이 없을때 사용할 로직 만들기
        # list out of range가 나오면 여기를 의심해야됨
        while (protein_buff_aver > 20 or fat_buff_aver > 20 or carbohydrate_buff_aver > 20):
            print("앙?")
            protein_buff_aver = 1
            fat_buff_aver = 1
            carbohydrate_buff_aver = 1
            
            with open('base/simul_data/diet_output.json') as f :
                simul_data = json.load(f)
            for data in simul_data.values():
                test_data = Meal_Calculation(data)
                meals_data = test_data.calc_meal(protein_buff, fat_buff, carbohydrate_buff)
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

            if self._check_buffer_20up(protein_buff_aver):
                protein_buff -= 0.1
            if self._check_buffer_20up(fat_buff_aver):
                fat_buff -= 0.1
            if self._check_buffer_20up(carbohydrate_buff_aver):
                carbohydrate_buff -= 0.1
            f.close()
            print(f"단 : {protein_buff_aver}")
            print(f"지 : {fat_buff_aver}")
            print(f"탄 : {carbohydrate_buff_aver}")
            print
        return protein_buff, fat_buff, carbohydrate_buff

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

