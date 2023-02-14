from rest_framework import serializers

from diet_meals.Utils.Diet_Calcuation import Diet_Calculator

class User_body_info_SZ(serializers.Serializer):
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=40, max_value=250)
    height = serializers.FloatField(min_value=140, max_value=250)

    gender = serializers.CharField(max_length=2)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)

    diet_status = serializers.FloatField(min_value=0.8, max_value=1.0)
    many_meals = serializers.IntegerField(min_value=2, max_value=3)
    
    def create(self, request, validated_data):
        instance = {}
        cal = Diet_Calculator(1.6, 0.28)
        cal.set_total_data(validated_data)
        instance["total_data"] = {}
        instance["total_data"] = cal.get_total_json_data()

        meals = validated_data["many_meals"]
        meals_ratio =  [0.25, 0.45, 0.3] if meals == 3 else [0.6, 0.4]
        meals_list = ["breakfast", "lunch", "dinner"] if meals == 3 else ["lunch", "dinner",]
        for i, meal in enumerate(meals_list) :
            instance[meal] = {}
            instance[meal]["kilo_calorie"] = round(instance["total_data"]["total_kilo_calorie"] * meals_ratio[i])
            instance[meal]["protein"] = round(instance["total_data"]["total_protein"] * meals_ratio[i])
            instance[meal]["fat"] = round(instance["total_data"]["total_fat"] * meals_ratio[i])
            instance[meal]["carbohydrate"] = round(instance["total_data"]["total_carbohydrate"] * meals_ratio[i])
        
        instance["diet_status"] = "다이어트" if validated_data["diet_status"] == 0.8 else "유지"
        return instance