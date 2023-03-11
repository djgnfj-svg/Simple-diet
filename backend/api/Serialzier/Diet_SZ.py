from rest_framework import serializers

from meals.Utils.Diet_Manager import Diet_Meal_Calculation_Manager


class Diet_SZ(serializers.Serializer):
    total_kcalorie = serializers.IntegerField()
    total_protein = serializers.IntegerField()
    total_fat = serializers.IntegerField()
    total_carbohydrate = serializers.IntegerField()

    diet_status = serializers.BooleanField()
    meal_count = serializers.IntegerField(min_value=1, max_value=4)

    def create(self, validated_data):
        diet_manager = Diet_Meal_Calculation_Manager(validated_data)
        diet_data = diet_manager.get_diet_meal()
        # todo : 영양소 초기화 로직 클래스 로직으로 처리하기
        diet_data["need_nutrient"] = {}
        for meal in diet_manager._meal_list:
            diet_data["need_nutrient"][meal] = diet_manager.get_meal(meal)
        return diet_data