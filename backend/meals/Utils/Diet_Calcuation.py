from meals.Utils.Diet_excption import init_Diet_total_data


class Diet_Calculator():
    '''
    
    '''
    def __init__(self, _protein_base_range=2.0, _fat_base_range=0.28) -> None:
        self._protein_base_range = _protein_base_range
        self._fat_base_range = _fat_base_range
        self.total_kcalorie = 0
        self.total_protein = 0
        self.total_fat = 0
        self.total_carbohydrate = 0

    def get_total_data(self):
        '''
        칼로리, 단백질, 지방, 탄수화물 순으로 리턴합니다.
        '''

        self.total_kcalorie
        return  self.total_kcalorie, self.total_protein, \
                self.total_fat, self.total_carbohydrate
    
    def get_total_json_data(self):
        '''
        {
            "total_kcalorie" : self.total_kcalorie
            "total_protein" : self.total_protein
            "total_fat" :  self.total_fat
            "total_carbohydrate" : self.total_carbohydrate
        }
        '''
        rtn = {}
        rtn["total_kcalorie"] = self.total_kcalorie
        rtn["total_protein"] = self.total_protein
        rtn["total_fat"] =  self.total_fat
        rtn["total_carbohydrate"] = self.total_carbohydrate
        return  rtn

    def Cal_diet(self, instance, meal_count, diet_status):
        meal_ratio = [0.25, 0.45, 0.3] if meal_count == 3 else [0.6, 0.4]
        meal_list = ["breakfast", "lunch", "dinner"] if meal_count == 3 else ["lunch", "dinner",]
        instance["diet_status"] = "다이어트" if diet_status == 0.8 else "유지"

        if not self.total_carbohydrate and not self.total_fat \
            and not self.total_protein and not self.total_kcalorie:
            raise init_Diet_total_data
        for i, meal in enumerate(meal_list):
            instance[meal] = {}
            instance[meal]["kcalorie"] = round(self.total_kcalorie * meal_ratio[i])
            instance[meal]["protein"] = round(self.total_protein * meal_ratio[i])
            instance[meal]["fat"] = round(self.total_fat * meal_ratio[i])
            instance[meal]["carbohydrate"] = round(self.total_carbohydrate * meal_ratio[i])
     

    def set_total_data(self, validated_data):
        self.total_kcalorie = self._get_total_kcalorie(validated_data)
        self.total_protein = self._get_total_protein(validated_data["weight"])
        self.total_fat = self._get_total_fat(self.total_kcalorie)
        self.total_carbohydrate = self._get_total_carbohydrate()

    def get_total_kcalorie(self):
        return self.total_kcalorie

    def get_total_protein(self):
        return self.total_protein

    def get_total_fat(self):
        return self.total_fat
        
    def get_total_carbohydrate(self):
        return self.total_carbohydrate

    def _get_total_kcalorie(self,validated_data):
        gender = validated_data["gender"]
        weight = validated_data["weight"]
        height = validated_data["height"]
        general_activities = validated_data["general_activities"]
        excise_activity = validated_data["excise_activity"]
        age = validated_data["age"]
        diet_staus = validated_data["diet_status"]

        # 기초대사량
        if gender == "M":
            basal_metabolic_rate = (88.4 + 13.4 * weight) + (4.8 * height) - (5.68* age)
        else :
            basal_metabolic_rate = (447.6 + 9.25 * weight) +(3.1 * height) - (4.33 * age)

        # 활동계수
        activity_coefficient = general_activities + excise_activity
        total_kcalorie = basal_metabolic_rate * activity_coefficient
        return round(total_kcalorie * diet_staus)

    def _get_total_protein(self, weight):
        total_protein = weight * self._protein_base_range
        return round(total_protein)

    def _get_total_fat(self, total_kcalorie):
        extra_value = self._fat_base_range
        return round((total_kcalorie * extra_value) // 9)

    def _get_total_carbohydrate(self):
        total_carbohydrate_kcal = \
        (self.total_kcalorie - \
            ((self.total_protein * 4) + (self.total_fat * 9)))

        total_carbohydrate_gram = total_carbohydrate_kcal / 4
        return round(total_carbohydrate_gram)