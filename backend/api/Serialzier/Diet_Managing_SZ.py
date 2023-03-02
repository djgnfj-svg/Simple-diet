from rest_framework import serializers

from meals.Utils.Diet_Manager import Diet_Meal_Calculation_Manager

class Diet_Managing_SZ(serializers.Serializer):
    total_kcalorie = serializers.IntegerField()
    total_protein = serializers.IntegerField()
    total_fat = serializers.IntegerField()
    total_carbohydrate = serializers.IntegerField()

    # todo : choice형태를 만들어서 카테고리중 한개를 고를수 있게 만들기 serialzier 를 만들면 가능하다...
    # protein_option = serializers.IntegerField()
    # fat_option = serializers.IntegerField()
    # carbohydrate_option = serializers.IntegerField()

    diet_status = serializers.BooleanField()
    meal_count = serializers.IntegerField()
    def create(self, request, validated_data):
        diet_manager = Diet_Meal_Calculation_Manager(validated_data)
        temp = diet_manager.calc_meal()
        return {}