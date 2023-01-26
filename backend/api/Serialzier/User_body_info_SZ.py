from rest_framework import serializers

from api.Utils.Metabolic_rate_Calk import Calculation

class User_body_info_SZ(serializers.Serializer):
    gender = serializers.CharField(max_length=2)
    weight = serializers.FloatField(max_value=300)
    height = serializers.FloatField(max_value=200)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)
    age = serializers.IntegerField(min_value=13, max_value=150)
    many_meals = serializers.IntegerField(min_value=2, max_value=3)
    
    def create(self, request, validated_data):
        instance = {}
        cal = Calculation(1.6, 0.28)
        instance["total_data"] = {}
        instance["total_data"]["total_kilo_calorie"] = cal.total_kilo_calorie(validated_data)
        instance["total_data"]["total_protein"] = cal.total_protein(validated_data["weight"])
        instance["total_data"]["total_fat"] =  cal.total_fat(instance["total_data"]["total_kilo_calorie"])
        instance["total_data"]["total_carbohydrate"] = cal.total_carbohydrate(instance)

        meals = validated_data["many_meals"]
        meals_ratio = [0.6, 0.4] if meals==2 else [0.25, 0.45, 0.3]

        meals_list = ["breakfast", "lunch", "dinner"]
        for i, meal in enumerate(meals_list) :
            instance[meal] = {}
            instance[meal]["kilo_calorie"] = round(instance["total_data"]["total_kilo_calorie"] * meals_ratio[i])
            instance[meal]["protein"] = round(instance["total_data"]["total_protein"] * meals_ratio[i])
            instance[meal]["fat"] = round(instance["total_data"]["total_fat"] * meals_ratio[i])
            instance[meal]["carbohydrate"] = round(instance["total_data"]["total_carbohydrate"] * meals_ratio[i])
        
        return instance