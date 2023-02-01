class Calculation():
    def __init__(self, protein_base_range=2.0, fat_base_range=0.28) -> None:
        self.protein_base_range = protein_base_range
        self.fat_base_range = fat_base_range

    def total_kilo_calorie(self,validated_data):
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

    def total_protein(self, weight):
        total_protein = weight * self.protein_base_range
        return round(total_protein)

    def total_fat(self, total_kilo_calorie):
        extra_value = self.fat_base_range
        return round((total_kilo_calorie * extra_value) // 9)

    def total_carbohydrate(self,instance):
        #나머지는 모두 탄수화물로 가야함
        total_kilo_calorie = instance["total_data"]["total_kilo_calorie"]
        total_protein = instance["total_data"]["total_protein"]
        total_fat = instance["total_data"]["total_fat"]
    
        total_carbohydrate_kcal = (total_kilo_calorie - ((total_protein * 4) + (total_fat * 9)))

        total_carbohydrate_gram = total_carbohydrate_kcal / 4
        return round(total_carbohydrate_gram)