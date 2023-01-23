from rest_framework import serializers

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

def Make_week_food_data(total_data):

    '''
    1. 끼니 데이터를 받는다.
    2. 음식데이터 중에 아침용을 정렬시킨다.
    3. 아침 데이터 단 - 지 - 탄 순으로 채운다.
    4. 오차가 얼마나 있는지 확인하고 각각의 최대치를 넘으면 조정하거나 다음식단의 가중치로 넣는다.
    5. 점심과 저녁데이터를 위와같이 진행한다.
        a. 만약 대용량일경우 1/2 1/3 을넣으면서 테스트 한다.
            대용량 -> 1개이면서 500g 이상
    6. 최종데이터를 점검한다.
    '''
    return 


class User_body_info_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self,request, validated_data):
        instance = {}
        '''
        // 이작업을 그러면 db가 갱신되거나 할때마다 해줘야하는데 ㅅㅂ sh파일로 만들든가 해야겠따.
        1. 토탈데이터와 끼니데이터 나누기 o
        2. 토탈데이터로 주간 데이터 구하기 o
        3. 주간데이터를 통해서 먹어야하는 주간음식데이터를 만든다
            주간 음식 데이터 만들기
        4. 나온 주간음식데이터를 일간으로 나눈다.
            큰용량은 2, 3으로 나눈다.

        5. 일간으로 나눈 음식데이터를 끼니별로 나눈다.
        6. 리턴한다리~
        ''' 
        print(validated_data)
        total_data, meal1_data, meal2_data, meal3_data = Classify_data(validated_data["data"])
        week_data = Cal_week_data(total_data)

        week_food_data = Make_week_food_data(total_data)
        instance = week_data
        return instance