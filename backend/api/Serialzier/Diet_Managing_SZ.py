from rest_framework import serializers
from diet_meals.Utils.Diet_Managing_utils import Diet_Manager


def Classify_data(data):
    total_data = data["total_data"]
    try :
        breakfast = data["breakfast"]
    except KeyError:
        breakfast = None
    lunch = data["lunch"]
    dinner = data["dinner"]
    return total_data, breakfast, lunch, dinner


class Diet_Managing_SZ(serializers.Serializer):
    # todo 데이터로 받는게 맞나...?
    data = serializers.JSONField()
    def create(self, request, validated_data):
        total_data, breakfast, lunch, dinner = Classify_data(validated_data["data"])
        diet_manager = Diet_Manager(breakfast, lunch, dinner)
        managing_diet = diet_manager.get_diet_info()
        
        return managing_diet