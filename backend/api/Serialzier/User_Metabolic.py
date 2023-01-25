from rest_framework import serializers
from api.Utils.Fodd_utils import Make_week_food_data

from foods.models import Food_data

# 유저에게 제공되는 식단을 저장할 것인가?
# 추세를 알기위해서 필요할 듯하다
# 나중에 알러지 같은 커스텀한 요소가 나온다면
# 쌓이는 데이터의 질이 좋아질 것으로 보인다.
# 일단 DB없이 가자

def Classify_data(data):
    total_data = data["total_data"]
    meal1_data, meal2_data, meal3_data = 0,0,0

    meals_data = data["meals"]
    meal1_data = meals_data["1_meals"]
    meal2_data = meals_data["2_meals"]
    meal3_data = meals_data["3_meals"]

    return total_data, meal1_data, meal2_data, meal3_data

def Cal_week_data(total_data):
    # 6일치의 식량을 준다
    # 7일은 소수여서 나누기 어렵고 일요일은 먹고픈거 먹으라는 깊은뜻
    week_data = {}
    week_data["week_kilo_calorie"] = total_data["total_kilo_calorie"] * 6
    week_data["week_protein"] = total_data["total_protein"] * 6
    week_data["week_fat"] = total_data["total_fat"] * 6
    week_data["week_carbohydrate"] = total_data["total_carbohydrate"] * 6
    return week_data


class User_body_info_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self,request, validated_data):
        '''
        1. 토탈데이터와 끼니데이터 나누기 o
        2. 토탈데이터로 주간 데이터 구하기 o
        3. 끼니별 음식 데이터를 구한다.
        4. 일에 먹어야하는 음식 데이터를 구한다.
        5. 
        6. 리턴한다리~
        ''' 
        total_data, breakfast, lunch, dinner = Classify_data(validated_data["data"])
        week_data = Cal_week_data(total_data)

        day_food_data = Make_week_food_data(total_data, breakfast, lunch, dinner)
        return day_food_data