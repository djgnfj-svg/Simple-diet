from django.db.models import Q

from foods.models import Food


class Food_Assign:
    def __init__(self) -> None:
        pass

    def _assign_food_nutrient(self, instance, food:Food, nutrient_cut, isdouble):
        if isdouble:
            instance["kcalorie"] = round(food.kcalorie * nutrient_cut)
            instance["protein"] = round(food.protein * nutrient_cut)
            instance["fat"] = round(food.fat * nutrient_cut)
            instance["carbohydrate"] = round(food.carbohydrate * nutrient_cut)
        else:
            instance["kcalorie"] = round(food.kcalorie / nutrient_cut)
            instance["protein"] = round(food.protein / nutrient_cut)
            instance["fat"] = round(food.fat / nutrient_cut)
            instance["carbohydrate"] = round(food.carbohydrate / nutrient_cut)

    def assign_food_data(self, food:Food, food_number, isdouble, nutrient_cut):
        instance = {}
        instance["food_name"] = food.name
        instance["food_link"] = food.link
        if isdouble:
            instance["food_number"] = food_number * 2
        else:
            instance["food_number"] = food_number
        self._assign_food_nutrient(instance, food, nutrient_cut, isdouble)
        return instance

    def add_food_nutrient(self, instance, food:Food, nutrient_cut, isdouble):
        double_value = 2 if isdouble else 1

        instance["kcalorie"] += round(food.kcalorie / nutrient_cut) * double_value
        instance["protein"] += round(food.protein / nutrient_cut) * double_value
        instance["fat"] += round(food.fat /nutrient_cut) * double_value 
        instance["carbohydrate"] += round(food.carbohydrate / nutrient_cut) * double_value


class Food_Checker(Food_Assign):
    def __init__(self) -> None:
        super().__init__()
        # TODO : ver0.9 매니져로 관리할 예정
        self._over_buffer = 1.2
        self._double_buffer = 2.0

    def _check_over_nutrient(self, food: Food, current_meal_nutrient,need_nutrient, nutrient):
        '''
        음식 영양소 + 현재식사 영양소 > 필요영양소 * 오버버퍼
        너무 많이 초과하면 다음 음식으로 넘어가는 로직
        '''
        food_nutrient = getattr(food, nutrient)
        if food_nutrient + current_meal_nutrient[nutrient] > \
            need_nutrient[nutrient] * self._over_buffer:
            return True
        return False

    def _check_double(self, food: Food, current_meal_nutrient,need_nutrient,  nutrient):
        '''
        음식영양소 * 버퍼, < 목표영양소 - 현재영양소
        음식을 2개로 해도 되는지 계산하는 로직입니다.
        '''
        food_nutrient = getattr(food, nutrient)
        if food_nutrient* self._double_buffer < \
            need_nutrient[nutrient] * current_meal_nutrient[nutrient]:
            return True
        return False


class Food_Manager(Food_Checker):
    def __init__(self) -> None:
        super().__init__()

    #TODO : ver0.9에 음식을 가져오는 로직 고도화
    def get_food(self, food_number, sort_nutrient):
        q = Q()

        rtn = Food.objects.filter(q)

        rtn = rtn.order_by("-"+sort_nutrient)
        return rtn[food_number]