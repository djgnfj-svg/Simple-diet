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

# todo : 현재는 프론트에서 어떡게 받는지 몰라서 data라는 형태로 받았지만
# 추후 수정예정이다.
class Diet_Managing_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self, request, validated_data):
        total_data, breakfast, lunch, dinner = Classify_data(validated_data["data"])
        diet_manager = Diet_Manager(breakfast, lunch, dinner)
        managing_diet = diet_manager.get_diet_info()
        managing_diet["breakfast_nutrient"] = breakfast
        managing_diet["lunch_nutrient"] = lunch
        managing_diet["dinner_nutrient"] = dinner
        return managing_diet