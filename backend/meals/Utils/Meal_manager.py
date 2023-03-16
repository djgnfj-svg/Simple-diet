from meals.Utils.Nutrient_Manager import Nutrient_Manager
from foods.models import Food

from meals.Utils.Food_Manager import Food_Manager


class Meals_Assign:
    def __init__(self, nutrient_diet_data) -> None:

        # 끼니 별로 데이터 나누기 좋은방법이 안떠올라 아래처럼 코딩하였다.
        if nutrient_diet_data["meal_count"] == 3:
            self._meal_ratio = [0.25, 0.45, 0.3]
            self._meal_list = ["breakfast", "lunch", "dinner"]
        elif nutrient_diet_data["meal_count"] == 2:
            self._meal_ratio = [0.6, 0.4]
            self._meal_list = ["breakfast", "lunch"]
        else:
            self._meal_ratio = [1]
            self._meal_list = ["breakfast"]

        _diet_cut = 0.8 if nutrient_diet_data["diet_status"] else 1
        total_kcalorie = nutrient_diet_data["total_kcalorie"] * _diet_cut
        total_protein = nutrient_diet_data["total_protein"] * _diet_cut
        total_fat = nutrient_diet_data["total_fat"] * _diet_cut
        total_carbohydrate = nutrient_diet_data["total_carbohydrate"] * _diet_cut

        self.meals = {}
        for i, meal in enumerate(self._meal_list):
            self.meals[meal] = {}
            self.meals[meal]["kcalorie"] = round(total_kcalorie * self._meal_ratio[i])
            self.meals[meal]["protein"] = round(total_protein * self._meal_ratio[i])
            self.meals[meal]["fat"] = round(total_fat * self._meal_ratio[i])
            self.meals[meal]["carbohydrate"] = round(total_carbohydrate * self._meal_ratio[i])

    def get_meal(self, meal):
        return self.meals[meal]


class Meal_Calculation(Meals_Assign):
    def __init__(self, nutrient_diet_data) -> None:
        Meals_Assign.__init__(self, nutrient_diet_data)

        if nutrient_diet_data["meal_count"] == 3:
            self.breakfast_need_nutrient = self.meals["breakfast"]
            self.lunch_need_nutrient = self.meals["lunch"]
            self.dinner_need_nutrient = self.meals["dinner"]

        elif nutrient_diet_data["meal_count"] == 2:
            self.breakfast_need_nutrient = self.meals["breakfast"]
            self.lunch_need_nutrient = self.meals["lunch"]
        else:
            self.breakfast_need_nutrient = self.meals["breakfast"]

    def _add_food_meal(self, meal_food_data, current_meal_nutrient, food: Food,
                            food_count, isdouble):
        # TODO : 좀더 정교한 로직이 필요할꺼라고 생각한다.(ver0.9)
        nutrient_cut = 1
        food_number = 1
        # TODO : 클래스 메서드 정적 메서드
        food_manager = Food_Manager()
        if isdouble:
            meal_food_data[str(food_count)] = food_manager.assign_food_data(
            food, food_number, isdouble, nutrient_cut)
            
        elif food.food_gram > 500:
            self._meal_have_bigsize_food = True
            if food.food_gram > 800:
                nutrient_cut = 3
                food_number = 0.3
            else:
                nutrient_cut = 2
                food_number = 0.5
        
        # 음식데이터 추가
        meal_food_data[str(food_count)] = food_manager.assign_food_data(
            food, food_number, isdouble, nutrient_cut)
        # 식단영양소에 추가
        food_manager.add_food_nutrient(current_meal_nutrient, food, nutrient_cut, isdouble)


    def calc_meal(self, protein_buff, fat_buff, carbohydrate_buff):
        diet_info = {}
        nutrient_list = ["protein", "fat", "carbohydrate"]
        food_manager = Food_Manager()
        for _, meal_name in enumerate(self._meal_list):
            meal_food_data = {}

            _protein_full = False
            _fat_full = False
            _carbohydrate_full = False
            _meal_have_bigsize_food = False

            current_meal_nutrient = {}
            current_meal_nutrient[meal_name] = Nutrient_Manager.init_nutrient()

            food_count = 0
            food_number = 0
            nutrient_focus = 0
            need_nutrient = getattr(self, f"{meal_name}_need_nutrient")
            while not _carbohydrate_full:
                food = food_manager.get_food(food_number,nutrient_list[nutrient_focus])

                if (food.food_gram > 500 and _meal_have_bigsize_food):
                    food_number += 1
                    continue
  
                if food_manager._check_over_nutrient(food, current_meal_nutrient[meal_name], need_nutrient, nutrient_list[nutrient_focus]):
                    food_number += 1
                    continue

                if  (food.food_gram < 500 and \
                    food_manager._check_double(food, current_meal_nutrient[meal_name], \
                    need_nutrient, nutrient_list[nutrient_focus])):
                    is_double = True
                else:
                    is_double = False

                #음식 추가
                meal_food_data[str(food_count)] = Nutrient_Manager.init_nutrient()
                self._add_food_meal(meal_food_data, current_meal_nutrient[meal_name], food, food_count, is_double)
                food_count += 1
                
                # 영양소가 만족했는가
                if Nutrient_Manager.check_nutrient_full(need_nutrient[nutrient_list[nutrient_focus]], protein_buff, current_meal_nutrient[meal_name][nutrient_list[nutrient_focus]]):
                    _protein_full=True
                    nutrient_focus = 1
                    if Nutrient_Manager.check_nutrient_full(need_nutrient[nutrient_list[nutrient_focus]], fat_buff, current_meal_nutrient[meal_name][nutrient_list[nutrient_focus]]):
                        _fat_full=True
                        nutrient_focus = 2
                        if Nutrient_Manager.check_nutrient_full(need_nutrient[nutrient_list[nutrient_focus]], carbohydrate_buff, current_meal_nutrient[meal_name][nutrient_list[nutrient_focus]]):
                            _carbohydrate_full=True
                            break
                    food_number = 0
            
            diet_info[meal_name] = meal_food_data
            diet_info[meal_name]["nutrient"] = current_meal_nutrient[meal_name]
        return diet_info
