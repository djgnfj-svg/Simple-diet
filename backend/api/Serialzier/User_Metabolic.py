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
    week_data = {}
    week_data["week_kilo_calorie"] = total_data["total_kilo_calorie"] * 6
    week_data["week_protein"] = total_data["total_protein"] * 6
    week_data["week_fat"] = total_data["total_fat"] * 6
    week_data["week_carbohydrate"] = total_data["total_carbohydrate"] * 6
    return week_data
class User_body_info_SZ(serializers.Serializer):
    data = serializers.JSONField()
    def create(self,request, validated_data):
        instance = {}
        '''
        // 이작업을 그러면 db가 갱신되거나 할때마다 해줘야하는데 ㅅㅂ sh파일로 만들든가 해야겠따.
        1. 토탈데이터와 끼니데이터 나누기 o
        2. 토탈데이터로 주간 데이터 구하기 o
        3. 주간데이터를 통해서 먹어야하는 주간음식데이터를 만든다
            음식데이터 모델을 만든다. o
            음식을 추가하는 API를 만든다.o
            음식을 추가할때 검증해야 하는 부분을 만든다 (링크중에 마지막넘버가 같으게 있으면 업데이트 창으로 간다거나)
                ex)
                주간 단백질 1000g
                우선순위에 따라서 측정하자 결국 DB Food 테이블에 우선순위는 존재해야한다.
                아니면 내가 그냥 가격순으로 정렬해 버리든가.

                여러개의 종목이 있는 품목에 대하여
                - 각각 더해서 평균을 정하는게 편할 듯 하다.
                그래
                - 주먹밥
                - 핫도그
                추가하자
               # 나중에 커스텀으로 식이섬유를 챙기시겠습니가?
                # 장점
                # 똥 굳
                # 단점
                # 가격, 보관
                분류를 따로 만들어야 하나?
                나중에 200개정도 됬을때 만들자
                그러면 저녁에 150이고 딱나누어 떨어지지 않으니까 200그람으로 나눈다
                월 저녁 200g ~~
                화 저녁 200g ~~

                이렇게 채우면 다른 음식을 넣든지 해야된다.
                큰거 해치우고 잔잔바리들 넣어야지
                메뉴는 3가지를 미만으로 한다.


        4. 나온 주간음식데이터를 일간으로 나눈다.
            큰용량은 2, 3으로 나눈다.

        5. 일간으로 나눈 음식데이터를 끼니별로 나눈다.
        6. 리턴한다리~
        ''' 
        total_data, meal1_data, meal2_data, meal3_data = Classify_data(validated_data["data"])
        week_data = Cal_week_data(total_data)

        print(week_data)
        instance = week_data
        return instance