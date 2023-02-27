from metabolic_calculator.models import Body_info, Metabolic
from meals.Utils.Diet_excption import init_Diet_total_data

class Metabolic_Calculator():
    def __init__(self, instance:Body_info, _protein_base_range=2.0, _fat_base_range=0.28) -> None:
        
        #todo : 만약 값이 안들어왔으면 
        # 매니져에서 값을 가져온다 매니져가 없다면 에러를 벴는다.
        self._protein_base_range = _protein_base_range
        self._fat_base_range = _fat_base_range
    
        self._cal_kcalorie(instance)
        self._cal_protein(instance.weight)
        self._cal_fat()
        self._cal_carbohydrate()

    def _cal_kcalorie(self, instance:Body_info):
        age = instance.age
        gender = instance.gender
        weight = instance.weight
        height = instance.height
        general_activities = instance.general_activities
        excise_activity = instance.excise_activity

        # 기초대사량
        if gender == "M":
            basal_metabolic_rate = (88.4 + 13.4 * weight) + (4.8 * height) - (5.68* age)
        else :
            basal_metabolic_rate = (447.6 + 9.25 * weight) +(3.1 * height) - (4.33 * age)
        activity_coefficient = general_activities + excise_activity
        self._total_kcalorie = round(basal_metabolic_rate * activity_coefficient)
        return self._total_kcalorie

    def _cal_protein(self, weight):
        self._total_protein = round(weight * self._protein_base_range)

    def _cal_fat(self):
        self._total_kcalorie
        self._total_fat = round((self._total_kcalorie * self._fat_base_range) // 9)
    
    def _cal_carbohydrate(self):
        self._total_kcalorie
        self._total_carbohydrate = self._total_kcalorie - \
            (self._total_protein * 4) - (self._total_fat * 9)

    @property
    def protein_base_range(self):
        return self._protein_base_range
    
    @protein_base_range.setter
    def protein_base_range(self, value:float):
        # todo : 이상한값 판별
        self._protein_base_range = value

    @property
    def fat_base_range(self):
        return self._fat_base_range
    
    @fat_base_range.setter
    def fat_base_range(self, value:float):
        # todo : 이상한값 판별
        self._fat_base_range = value

    @property
    def total_protein(self):
        return self._total_protein
    
    @property
    def total_fat(self):
        return self._total_fat
    
    @property
    def total_carbohydrate(self):
        return self._total_carbohydrate
    
    @property
    def total_kcalorie(self):
        return self._total_kcalorie

class Diet_Calculator():
    def __init__(self) -> None:
        pass

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
    