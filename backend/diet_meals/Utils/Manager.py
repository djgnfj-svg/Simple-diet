from django.db.models import Q

from foods.models import Food_data


class Manager():
    def __init__(self) -> None:
        pass


class Food_Manager(Manager):
    def __init__(self) -> None:
        pass

    # todo : 카테고리 등 음식을 가져오는 기능이 추가 될 것이다.
    def _get_food(self, meal, food_count):
        if meal == "breakfast":
            meal = 0
        elif meal == "lunch":
            meal = 1
        else:
            meal = 2

        # todo : 음식을 가져오는 조건을 더 까다롭게 할 예정이다
        q = Q()
        q &= Q(meals_fucus__icontains=meal)

        rtn = Food_data.objects.filter(q)

        # todo : 위의 정렬에따라서 정렬이 바뀔 수도 있다.
        sort_nutrient = ""
        if not self._protein_full:
            sort_nutrient = "-protein"
        elif not self._fat_full:
            sort_nutrient = "-fat"
        elif not self._carbohydrate_full:
            sort_nutrient = "-carbohydrate"
        else:
            self._check_nutrient_full = True
        rtn = rtn.order_by(sort_nutrient)
        return rtn[food_count]

    def _set_meal_food_data(self, food, big_size, food_number, double_value):
        instance = {}
        instance["food_name"] = food.name
        instance["food_link"] = food.link
        instance["kcalorie"] = round(food.kcalorie / big_size) * double_value
        instance["protein"] = round(food.protein/big_size) * double_value
        instance["fat"] = round(food.fat/big_size) * double_value
        instance["carbohydrate"] = round(
            food.carbohydrate/big_size) * double_value
        instance["food_number"] = food_number * double_value
        return instance


class Meal_Manager(Manager):
    def __init__(self) -> None:
        # 영양소 체크
        self._check_nutrient_full = False
        self._protein_full = False
        self._fat_full = False
        self._carbohydrate_full = False

    def _init_meal_nutrient_data(self):
        meals_data = {}
        meals_data["kcalorie"] = 0
        meals_data["protein"] = 0
        meals_data["fat"] = 0
        meals_data["carbohydrate"] = 0
        return meals_data
