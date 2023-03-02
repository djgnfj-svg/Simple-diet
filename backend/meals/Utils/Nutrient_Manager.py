
from foods.models import Food

# 영양소 초기화용
class Nutrient_data_initialization:
    def __init__(self) -> None:
        pass

    def _init_nutrient_data(self):
        meals_data = {}
        meals_data["kcalorie"] = 0
        meals_data["protein"] = 0
        meals_data["fat"] = 0
        meals_data["carbohydrate"] = 0
        return meals_data

    def _set_meal_nutrient_data(self, meal_nutrient_data, food_data, big_size, double_value):
        meal_nutrient_data["kcalorie"] += round(food_data.kcalorie / big_size) * double_value
        meal_nutrient_data["protein"] += round(food_data.protein / big_size) * double_value
        meal_nutrient_data["fat"] += round(food_data.fat /big_size) * double_value 
        meal_nutrient_data["carbohydrate"] += round(food_data.carbohydrate / big_size) * double_value

# todo : 음식 양양소 체크용 / 클래스 사용처가 이름과 너무 다름
class Nutrient_data_Checker(Nutrient_data_initialization):
    def __init__(self) -> None:
        super().__init__()
        self._food_over_buffer = 1.5
        self._food_double_buffer = 2.0

    def _check_food_over_nutrient(self, food: Food, meal_name, meal_nutrient_data):
        '''
        음식을 추가했을시 너무 높게 초과된다면 다음 음식을 추가한다.
        현재영양소 + 추가할 음식 영양소 > 채워야하는 영양소 * 버퍼
        '''
        # 채워야 하는 영양소
        if meal_name == "breakfast":
            nutrient_data = self.breakfast
        elif meal_name == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        # 채워야하는 영양소 확인
        temp = meal_nutrient_data[meal_name]
        if not self._protein_full:
            return food.protein + temp["protein"] > \
                nutrient_data["protein"] * self._food_over_buffer
        elif not self._fat_full:
            return food.fat + temp["fat"] > \
                nutrient_data["fat"] * self._food_over_buffer
        elif not self._carbohydrate_full:
            return food.carbohydrate + temp["carbohydrate"] > \
                nutrient_data["carbohydrate"] * self._food_over_buffer
        return False

    def _check_food_double(self, food: Food, meal_name, meal_nutrient_data):
        '''
        음식영양소 * 버퍼, < 목표영양소 - 현재영양소
        '''
        if meal_name == "breakfast":
            nutrient_data = self.breakfast
        elif meal_name == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        temp = meal_nutrient_data[meal_name]
        # todo big_size일 경우 처리가 안됨
        if not self._protein_full:
            return food.protein * self._food_double_buffer < \
                nutrient_data["protein"] - temp["protein"]
        elif not self._fat_full:
            return food.fat * self._food_double_buffer < \
                nutrient_data["fat"] - temp["fat"]
        elif not self._carbohydrate_full:
            return food.carbohydrate * self._food_double_buffer < \
                nutrient_data["carbohydrate"] - temp["carbohydrate"]
        return False

    #todo : fucus를 하나올리는 것을 여기에 넣는것은 좀...
    def _check_nutrient(self, meal, meal_nutrient_data, food_focus, 
                        protein_buff, fat_buff, carbohydrate_buff):
        '''
        채워야하는양 * 버퍼 < 현재 채워진양  
        '''
        # todo : 함수화 해야됨
        if meal == "breakfast":
            nutrient_data = self.breakfast
        elif meal == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        temp = meal_nutrient_data[meal]
        if nutrient_data["protein"] * protein_buff< temp["protein"] and not self._protein_full:
            self._protein_full = True
            return 0
        elif nutrient_data["fat"] * fat_buff < temp["fat"] and not self._fat_full:
            self._fat_full = True
            return 0
        elif nutrient_data["carbohydrate"] * carbohydrate_buff < temp["carbohydrate"]:
            self._carbohydrate_full = True
            return 0
        return food_focus+1  # todo : 여기서 0이 리턴되는 것도 문제이다.

