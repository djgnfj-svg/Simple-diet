from rest_framework import serializers
from api.Utils.Food_utils import Make_week_food_data


def Classify_data(data):
    total_data = data["total_data"]
    try :
        breakfast = data["breakfast"]
    except KeyError:
        breakfast = None
    lunch = data["lunch"]
    dinner = data["dinner"]
    return total_data, breakfast, lunch, dinner


class User_body_info_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self, request, validated_data):
        total_data, breakfast, lunch, dinner = Classify_data(validated_data["data"])
        day_food_data = Make_week_food_data(total_data, breakfast, lunch, dinner)
        
        return day_food_data