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
                    https://www.coupang.com/vp/products/6081081115?itemId=11273250763&vendorItemId=78550136737&q=%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4&itemsCount=36&searchId=076cfec654e54360884faba93b51e591&rank=3&isAddedCart=
                    https://www.coupang.com/vp/products/1519330646?itemId=5810607566&vendorItemId=73109054725&pickType=COU_PICK&q=%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4&itemsCount=36&searchId=076cfec654e54360884faba93b51e591&rank=2&isAddedCart=
                    https://www.coupang.com/vp/products/4656203901?itemId=5810700340&vendorItemId=73109147042&q=%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4&itemsCount=36&searchId=076cfec654e54360884faba93b51e591&rank=1&isAddedCart=
                2. 야채...?
                    토마토
                    아보카도
                3. 냉동식품 - 육류
                    https://www.coupang.com/vp/products/1271810164?itemId=2276602192&vendorItemId=70273767100&q=%EB%83%89%EB%8F%99%EC%8B%9D%ED%92%88&itemsCount=36&searchId=6faaadf02aeb4b498d36213557fe1c01&rank=1&isAddedCart=
                    https://www.coupang.com/vp/products/1608824364?itemId=2747730175&vendorItemId=70737703048&q=%EB%83%89%EB%8F%99%EC%8B%9D%ED%92%88&itemsCount=36&searchId=6faaadf02aeb4b498d36213557fe1c01&rank=3&isAddedCart=
                    https://www.coupang.com/vp/products/4567751809?itemId=5575412259&vendorItemId=72874737915&q=%EB%83%89%EB%8F%99%EC%8B%9D%ED%92%88&itemsCount=36&searchId=6faaadf02aeb4b498d36213557fe1c01&rank=6&isAddedCart=
                    https://www.coupang.com/vp/products/1583514552?itemId=2706863599&vendorItemId=70697150399&q=%EB%83%89%EB%8F%99%EC%8B%9D%ED%92%88&itemsCount=36&searchId=6faaadf02aeb4b498d36213557fe1c01&rank=7&isAddedCart=
                4. 즉석밥
                    https://www.coupang.com/vp/products/1391921882?itemId=2427315006&vendorItemId=70421315511&pickType=COU_PICK&q=%EA%B3%A4%EC%95%BD+%EC%A6%89%EC%84%9D%EB%B0%A5&itemsCount=36&searchId=2c0b8311e158402fb3d0c62fbe417d1a&rank=1&isAddedCart=
                    https://www.coupang.com/vp/products/1391921882?itemId=2427315006&vendorItemId=70421315511&pickType=COU_PICK&q=%EA%B3%A4%EC%95%BD+%EC%A6%89%EC%84%9D%EB%B0%A5&itemsCount=36&searchId=2c0b8311e158402fb3d0c62fbe417d1a&rank=1&isAddedCart=
                    https://www.coupang.com/vp/products/78749832?itemId=550725955&vendorItemId=84639394011&q=%EC%A6%89%EC%84%9D%EB%B0%A5&itemsCount=36&searchId=f9285b586a9a491f96772e257ea38043&rank=15&isAddedCart=
                5. 그냥 소세지
                    https://www.coupang.com/vp/products/346980667?itemId=1101451330&vendorItemId=5629539835&q=%EC%86%8C%EC%84%B8%EC%A7%80&itemsCount=36&searchId=b49e2e8c93f94cb39f8f34f4fa1c1778&rank=9&isAddedCart=
                    https://www.coupang.com/vp/products/2124428252?itemId=3604872129&vendorItemId=71590545160&q=%EC%86%8C%EC%84%B8%EC%A7%80&itemsCount=36&searchId=b49e2e8c93f94cb39f8f34f4fa1c1778&rank=3&isAddedCart=
                    https://www.coupang.com/vp/products/1756604528?itemId=2991836703&vendorItemId=70980135976&pickType=COU_PICK&q=%EC%86%8C%EC%84%B8%EC%A7%80&itemsCount=36&searchId=b49e2e8c93f94cb39f8f34f4fa1c1778&rank=0&isAddedCart=
                6. 닭가슴살 스테이크
                    https://www.coupang.com/vp/products/2171896373?itemId=3694584054&vendorItemId=71679890952&q=%EB%8B%AC%EA%B0%80%EC%8A%B4%EC%82%B4+%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%81%AC&itemsCount=36&searchId=8806b4a9b3d6414395b1a74a1c7473d2&rank=1&isAddedCart=
                    https://www.coupang.com/vp/products/4926123653?itemId=6464747257&vendorItemId=73759176633&q=%EB%8B%AC%EA%B0%80%EC%8A%B4%EC%82%B4+%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%81%AC&itemsCount=36&searchId=8806b4a9b3d6414395b1a74a1c7473d2&rank=2&isAddedCart=
                    https://www.coupang.com/vp/products/343254008?itemId=1090857293&vendorItemId=5252253109&q=%EB%8B%AC%EA%B0%80%EC%8A%B4%EC%82%B4+%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%81%AC&itemsCount=36&searchId=8806b4a9b3d6414395b1a74a1c7473d2&rank=3&isAddedCart=
                7. 닭가슴살 소세지
                    https://www.coupang.com/vp/products/1915681699?itemId=3252475357&vendorItemId=71239553158&q=%EB%8B%AC%EA%B0%80%EC%8A%B4%EC%82%B4+%EC%86%8C%EC%84%B8%EC%A7%80&itemsCount=36&searchId=08cc6cf8df0c4181b236570c0d065e7d&rank=2&isAddedCart=
                8. 냉동 볶음밥
                    https://www.coupang.com/vp/products/185917324?itemId=983874261&vendorItemId=5510637232&pickType=COU_PICK&q=%EB%B3%B6%EC%9D%8C%EB%B0%A5&itemsCount=36&searchId=4907a46a41e448dca1bf5251b3738ab5&rank=1&isAddedCart=
                    https://www.coupang.com/vp/products/1310396687?itemId=2327020830&vendorItemId=70323614197&q=%EB%B3%B6%EC%9D%8C%EB%B0%A5&itemsCount=36&searchId=4907a46a41e448dca1bf5251b3738ab5&rank=6&isAddedCart=
                    https://www.coupang.com/vp/products/343228726?itemId=1090788751&vendorItemId=5604190721&q=%EB%B3%B6%EC%9D%8C%EB%B0%A5&itemsCount=36&searchId=4907a46a41e448dca1bf5251b3738ab5&rank=7&isAddedCart=
                    https://www.coupang.com/vp/products/6072624005?itemId=11218284903&vendorItemId=78495771839&pickType=COU_PICK&q=%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8+%EA%B0%84%EB%8B%A8%EC%8B%9D%ED%92%88&itemsCount=36&searchId=276d4fc1679d4ddfa7150fd362c8cd1d&rank=1&isAddedCart=
                9. 크래미
                    https://www.coupang.com/vp/products/280767413?itemId=891150359&vendorItemId=5242710854&pickType=COU_PICK&q=%ED%81%AC%EB%9E%98%EB%AF%B8&itemsCount=36&searchId=932963c88a484575b4e4b3a70ff89042&rank=0&isAddedCart=
                    https://www.coupang.com/vp/products/280767362?itemId=891150262&vendorItemId=5242710682&q=%ED%81%AC%EB%9E%98%EB%AF%B8&itemsCount=36&searchId=932963c88a484575b4e4b3a70ff89042&rank=1&isAddedCart=
                10. 다이어트 도시락
                    https://www.coupang.com/vp/products/293454508?itemId=926514679&vendorItemId=5302343324&q=%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8+%EA%B0%84%EB%8B%A8%EC%8B%9D%ED%92%88&itemsCount=36&searchId=276d4fc1679d4ddfa7150fd362c8cd1d&rank=3&isAddedCart=
                    https://www.coupang.com/vp/products/6373068955?itemId=13507557295&vendorItemId=80761641301&q=%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8+%EA%B0%84%EB%8B%A8%EC%8B%9D%ED%92%88&itemsCount=36&searchId=276d4fc1679d4ddfa7150fd362c8cd1d&rank=7&isAddedCart=
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