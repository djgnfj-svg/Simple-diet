from rest_framework import serializers

from meals.Utils.Diet_Manager import Diet_Meal_Calculation_Manager


class Diet_Managing_SZ(serializers.Serializer):
    total_kcalorie = serializers.IntegerField()
    total_protein = serializers.IntegerField()
    total_fat = serializers.IntegerField()
    total_carbohydrate = serializers.IntegerField()

    diet_status = serializers.BooleanField()
    meal_count = serializers.IntegerField()
    def create(self, request, validated_data):
        diet_manager = Diet_Meal_Calculation_Manager(validated_data)
        diet_data = diet_manager.get_diet_meal()
        diet_data["need_nutrient"] = {}
        for meal in diet_manager._meal_list:
            diet_data["need_nutrient"][meal] = diet_manager.get_meal(meal)
        return diet_data