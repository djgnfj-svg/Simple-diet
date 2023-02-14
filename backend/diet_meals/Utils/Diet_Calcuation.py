class Diet_Calculator():
    def __init__(self, __protein_base_range=2.0, __fat_base_range=0.28) -> None:
        self.__protein_base_range = __protein_base_range
        self.__fat_base_range = __fat_base_range
        self.total_kilo_calorie = 0
        self.total_protein = 0
        self.total_fat = 0
        self.total_carbohydrate = 0

    
    def get_total_data(self):
        '''
        칼로리, 단백질, 지방, 탄수화물 순으로 리턴합니다.
        '''

        self.total_kilo_calorie
        return  self.total_kilo_calorie, self.total_protein, \
                self.total_fat, self.total_carbohydrate
    def get_total_json_data(self):
        '''
        {
            "total_kilo_calorie" : self.total_kilo_calorie
            "total_protein" : self.total_protein
            "total_fat" :  self.total_fat
            "total_carbohydrate" : self.total_carbohydrate
        }
        '''
        rtn = {}
        rtn["total_kilo_calorie"] = self.total_kilo_calorie
        rtn["total_protein"] = self.total_protein
        rtn["total_fat"] =  self.total_fat
        rtn["total_carbohydrate"] = self.total_carbohydrate
        return  rtn

    
    def set_total_data(self, validated_data):
        self.total_kilo_calorie = self._get_total_kilo_calorie(validated_data)
        self.total_protein = self._get_total_protein(validated_data["weight"])
        self.total_fat = self._get_total_fat(self.total_kilo_calorie)
        self.total_carbohydrate = self._get_total_carbohydrate()

    def get_total_kilo_calorie(self):
        return self.total_kilo_calorie

    def get_total_protein(self):
        return self.total_protein

    def get_total_fat(self):
        return self.total_fat
        
    def get_total_carbohydrate(self):
        return self.total_carbohydrate

    def _get_total_kilo_calorie(self,validated_data):
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
        total_kilo_calorie = basal_metabolic_rate * activity_coefficient
        return round(total_kilo_calorie * diet_staus)

    def _get_total_protein(self, weight):
        total_protein = weight * self.__protein_base_range
        return round(total_protein)

    def _get_total_fat(self, total_kilo_calorie):
        extra_value = self.__fat_base_range
        return round((total_kilo_calorie * extra_value) // 9)

    def _get_total_carbohydrate(self):
        total_carbohydrate_kcal = \
        (self.total_kilo_calorie - \
            ((self.total_protein * 4) + (self.total_fat * 9)))

        total_carbohydrate_gram = total_carbohydrate_kcal / 4
        return round(total_carbohydrate_gram)