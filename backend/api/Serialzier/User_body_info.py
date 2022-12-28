from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.Utils.Metabolic_rate_Calk import Calculation

class User_body_info(serializers.Serializer):
    # choice로 할지는 고민
    gender = serializers.CharField(max_length=2)
    weight = serializers.FloatField(max_value=300)
    height = serializers.FloatField(max_value=200)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)
    age = serializers.IntegerField(min_value=13, max_value=150)
    many_meals = serializers.IntegerField(min_value=2, max_value=3)
    
    def create(self, request, validated_data):
        instance = {}
        meals = validated_data["many_meals"]
        cal = Calculation()
        instance["total_data"] = {}
        instance["total_data"]["total_kilo_calorie"] = cal.total_kilo_calorie(validated_data)
        instance["total_data"]["total_protein"] = cal.total_protein(validated_data)
        instance["total_data"]["total_fat"] =  cal.total_fat(instance["total_data"]["total_kilo_calorie"])
        instance["total_data"]["total_carbohydrate"] = cal.total_carbohydrate(instance)

        instance["meals"] = {}
        if meals == 2:
            meals_ratio = [0.6, 0.4]
        else :
            meals_ratio = [0.25, 0.45, 0.3]

        for i in range(1, meals + 1) :
            instance["meals"][str(i) + "_meals"] = {}
            instance["meals"][str(i) + "_meals"]["kilo_calorie"] = round(instance["total_data"]["total_kilo_calorie"] * meals_ratio[i-1])
            instance["meals"][str(i) + "_meals"]["protein"] = round(instance["total_data"]["total_protein"] * meals_ratio[i-1])
            instance["meals"][str(i) + "_meals"]["fat"] = round(instance["total_data"]["total_fat"] * meals_ratio[i-1])
            instance["meals"][str(i) + "_meals"]["carbohydrate"] = round(instance["total_data"]["total_carbohydrate"] * meals_ratio[i-1])
        return instance

    # def validate_gender(self, value):
    #     if "M" not in value:
    #         raise ValidationError("성별 데이터가 잘못됬습니다.")
    #     return value