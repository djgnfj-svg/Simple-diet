class Calculation():
    def total_kilo_calorie(self,validated_data):
        gender = validated_data["gender"]
        weight = validated_data["weight"]
        height = validated_data["height"]
        general_activities = validated_data["general_activities"]
        excise_activity = validated_data["excise_activity"]
        age = validated_data["age"]

        # 나중에 체중증량을 생각해서 변수를 만들어주었다.
        is_lose = True

        # 기초대사량
        if gender == "M":
            basal_metabolic_rate = (88.4 + 13.4 * weight) + (4.8 * height) - (5.68* age)
        else :
            basal_metabolic_rate = (447.6 + 9.25 * weight) +(3.1 * height) - (4.33 * age)

        # 활동계수
        activity_coefficient = general_activities + excise_activity

        total_kilo_calorie = basal_metabolic_rate * activity_coefficient

        if is_lose :
            return round(total_kilo_calorie * 0.8)
        else :
            return round(total_kilo_calorie)

    def total_protein(self, validated_data):
        weight = validated_data["weight"]
        excise_activity =  validated_data["excise_activity"]

        extra_value = 2.0 # 1.6 ~ 2.2 중간값이다.

        if 0.3 <= excise_activity:
            extra_value = 2.5

        total_protein = weight * extra_value
        return round(total_protein)

    def total_fat(self, total_kilo_calorie):
        # 20% 35% 까지 권장한다 나중에 여부를 확인할 수 있도록 만들자
        extra_value = 0.3
        # if 지방을 선호하지 않으면 ~
        return round((total_kilo_calorie * extra_value) / 9)

    def total_carbohydrate(self,instance):
        #나머지는 모두 탄수화물로 가야함
        total_kilo_calorie = instance["total_data"]["total_kilo_calorie"]
        total_protein = instance["total_data"]["total_protein"]
        total_fat = instance["total_data"]["total_fat"]
    
        total_carbohydrate = (total_kilo_calorie - ((total_protein * 4) + (total_fat * 9)))

        total_carbohydrate = total_carbohydrate / 4
        return round(total_carbohydrate)