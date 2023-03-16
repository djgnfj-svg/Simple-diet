from rest_framework import serializers
from foods.models import Food

from meals.models import Meal

from meals.Utils.Diet_Manager import Diet_Maker

class Diet_SZ(serializers.Serializer):
    total_kcalorie = serializers.IntegerField()
    total_protein = serializers.IntegerField()
    total_fat = serializers.IntegerField()
    total_carbohydrate = serializers.IntegerField()

    diet_status = serializers.BooleanField()
    meal_count = serializers.IntegerField(min_value=1, max_value=4)

    def create(self, validated_data):
        diet_manager = Diet_Maker(validated_data)
        diet = diet_manager.get_diet()
        # TODO : 저장 로직만들기

        # meals_instance = Meals.objects.createa()
        # meal_list = []
        for meal_name in diet:
            # 음식의 id들을 구한다.
            # filter를 통해서 음식 리스트를 구한다.
            # 삽입하여서
            food_name_list = diet_manager.get_meal_foods(meal_name)
            foods = Food.objects.filter(name__in = food_name_list)
            instance = Meal.objects.create(
                meal_name = meal_name,

            )
            instance.foods.set(foods)
            # meal_list.append(instance.id)
        # meals_instance.meal.set(meal_lsit)
        need_nutrient = {}
        for meal in diet:
            need_nutrient[meal] = diet_manager.get_meal(meal)
        diet["need_nutrient"] = need_nutrient
        return diet