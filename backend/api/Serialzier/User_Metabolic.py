from rest_framework import serializers
from api.Utils.Fodd_utils import Make_week_food_data


def Classify_data(data):
    total_data = data["total_data"]
    breakfast = data["breakfast"]
    lunch = data["lunch"]
    dinner = data["dinner"]

    return total_data, breakfast, lunch, dinner

# 6일치의 식량을 리턴한다.
def init_week_data(total_data):
    week_data = {}
    week_data["week_kilo_calorie"] = total_data["total_kilo_calorie"] * 6
    week_data["week_protein"] = total_data["total_protein"] * 6
    week_data["week_fat"] = total_data["total_fat"] * 6
    week_data["week_carbohydrate"] = total_data["total_carbohydrate"] * 6
    return week_data


class User_body_info_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self, request, validated_data):
        total_data, breakfast, lunch, dinner = Classify_data(validated_data["data"])
        print(breakfast)
        week_data = init_week_data(total_data)

        day_food_data = Make_week_food_data(total_data, breakfast, lunch, dinner)
        return day_food_data