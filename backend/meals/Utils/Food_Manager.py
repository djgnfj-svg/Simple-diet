from django.db.models import Q

from foods.models import Food

from meals.Utils.Nutrient_Manager import Nutrient_Checker


# 음식 계산용
class Food_Calculator(Nutrient_Checker):
    def __init__(self) -> None:
        super().__init__()
        # todo : 매니져로 거시기 할 수 있음
        self._food_over_buffer = 1.5
        self._food_double_buffer = 2.0

    def _check_food_over_nutrient(self, food: Food, meal_name, current_meal_nutrient):
        '''
        음식을 추가했을시 너무 높게 초과된다면 다음 음식을 추가한다.
        현재영양소 + 추가할 음식 영양소 > 채워야하는 영양소 * 버퍼
        '''
        need_nutrient = getattr(self, f"{meal_name}_need_nutrient", None)
        if need_nutrient is None:
            return False

        temp = current_meal_nutrient[meal_name]
        if not self._protein_full:
            return food.protein + temp["protein"] > \
                need_nutrient["protein"] * self._food_over_buffer
        elif not self._fat_full:
            return food.fat + temp["fat"] > \
                need_nutrient["fat"] * self._food_over_buffer
        elif not self._carbohydrate_full:
            return food.carbohydrate + temp["carbohydrate"] > \
                need_nutrient["carbohydrate"] * self._food_over_buffer
        return False

    def _check_food_double(self, food: Food, meal_name, current_meal_nutrient):
        '''
        음식영양소 * 버퍼, < 목표영양소 - 현재영양소
        '''
        need_nutrient = getattr(self, f"{meal_name}_need_nutrient", None)
        if need_nutrient is None:
            return False

        temp = current_meal_nutrient[meal_name]
        if not self._protein_full:
            return food.protein * self._food_double_buffer < \
                need_nutrient["protein"] - temp["protein"]
        elif not self._fat_full:
            return food.fat * self._food_double_buffer < \
                need_nutrient["fat"] - temp["fat"]
        elif not self._carbohydrate_full:
            return food.carbohydrate * self._food_double_buffer < \
                need_nutrient["carbohydrate"] - temp["carbohydrate"]
        return False

    def _assign_meal_food_data(self, food, big_size, food_number, double_value):
        instance = {}
        temp =food_number * double_value
        instance["food_name"] = food.name
        instance["food_link"] = food.link
        instance["kcalorie"] = round(food.kcalorie / big_size) * double_value
        instance["protein"] = round(food.protein/big_size) * double_value
        instance["fat"] = round(food.fat/big_size) * double_value
        instance["carbohydrate"] = round(
            food.carbohydrate/big_size) * double_value
        instance["food_number"] = food_number * double_value
        return instance

    def _assign_food_nutrient(self, meal_nutrient_data, food_data, big_size, double_value):
        meal_nutrient_data["kcalorie"] += round(food_data.kcalorie / big_size) * double_value
        meal_nutrient_data["protein"] += round(food_data.protein / big_size) * double_value
        meal_nutrient_data["fat"] += round(food_data.fat /big_size) * double_value 
        meal_nutrient_data["carbohydrate"] += round(food_data.carbohydrate / big_size) * double_value

# 음식 가져오기용
class Food_Manager(Food_Calculator):
    def __init__(self) -> None:
        super().__init__()

    def _get_food(self, meal, food_count):
        if meal == "breakfast":
            meal = 0
        elif meal == "lunch":
            meal = 1
        else:
            meal = 2

        q = Q()
        q &= Q(meals_fucus__icontains=meal)

        rtn = Food.objects.filter(q)

        sort_nutrient = ""
        if not self._protein_full:
            sort_nutrient = "-protein"
        elif not self._fat_full:
            sort_nutrient = "-fat"
        elif not self._carbohydrate_full:
            sort_nutrient = "-carbohydrate"
        rtn = rtn.order_by(sort_nutrient)
        return rtn[food_count]