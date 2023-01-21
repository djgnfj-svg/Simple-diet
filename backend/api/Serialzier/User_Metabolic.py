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
            음식을 30개 정도 추가한다 <- ㅈㄴ힘든데? ㅋㅋㅋㅋ
                ex)
                주간 단백질 1000g
                우선순위에 따라서 측정하자 결국 DB Food 테이블에 우선순위는 존재해야한다.
                아니면 내가 그냥 가격순으로 정렬해 버리든가.
                1. 닭가슴살
                    https://www.coupang.com/vp/products/6081081115?itemId=11273250763
                    https://www.coupang.com/vp/products/1519330646?itemId=5810607566
                    https://www.coupang.com/vp/products/4656203901?itemId=5810700340
                2. 야채...?
                    토마토
                    아보카도
                3. 냉동식품 - 육류
                    https://www.coupang.com/vp/products/1271810164?itemId=2276602192
                    https://www.coupang.com/vp/products/1608824364?itemId=2747730175
                    https://www.coupang.com/vp/products/4567751809?itemId=5575412259
                    https://www.coupang.com/vp/products/1583514552?itemId=2706863599
                4. 즉석밥
                    https://www.coupang.com/vp/products/1391921882?itemId=2427315006
                    https://www.coupang.com/vp/products/78749832?itemId=550725955
                5. 그냥 소세지
                    https://www.coupang.com/vp/products/346980667?itemId=1101451330
                    https://www.coupang.com/vp/products/2124428252?itemId=3604872129
                    https://www.coupang.com/vp/products/1756604528?itemId=2991836703
                6. 닭가슴살 스테이크
                    https://www.coupang.com/vp/products/2171896373?itemId=3694584054
                    https://www.coupang.com/vp/products/4926123653?itemId=6464747257
                    https://www.coupang.com/vp/products/343254008?itemId=1090857293
                7. 닭가슴살 소세지
                    https://www.coupang.com/vp/products/1915681699?itemId=3252475357
                8. 냉동 볶음밥
                    https://www.coupang.com/vp/products/185917324?itemId=983874261
                    https://www.coupang.com/vp/products/1310396687?itemId=2327020830
                    https://www.coupang.com/vp/products/343228726?itemId=1090788751
                    https://www.coupang.com/vp/products/6072624005?itemId=11218284903
                9. 크래미
                    https://www.coupang.com/vp/products/280767413?itemId=891150359
                    https://www.coupang.com/vp/products/280767362?itemId=891150262
                10. 다이어트 도시락
                    https://www.coupang.com/vp/products/293454508?itemId=926514679
                    https://www.coupang.com/vp/products/6373068955?itemId=13507557295
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