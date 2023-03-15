class Nutrient_Assign:
    def __init__(self) -> None:
        pass

    def _init_nutrient(self):
        nuturient = {}
        nuturient["kcalorie"] = 0
        nuturient["protein"] = 0
        nuturient["fat"] = 0
        nuturient["carbohydrate"] = 0
        return nuturient
    
class Nutrient_Checker(Nutrient_Assign):
    def __init__(self) -> None:
        super().__init__()

    def _check_nutrient_all_full(self, meal_name, current_meal_nutrient, 
                        protein_buff, fat_buff, carbohydrate_buff):
        '''
        채워야하는양 * 버퍼 < 현재 채워진양  
        '''
        need_nutrient = getattr(self, f"{meal_name}_need_nutrient", None)
        if need_nutrient is None:
            return False
        
        # todo : 깔끔하게
        if self._check_nutrient_full(need_nutrient["protein"], protein_buff, current_meal_nutrient["protein"]):
            self._protein_full = True
            if self._check_nutrient_full(need_nutrient["fat"], fat_buff, current_meal_nutrient["fat"]):
                self._fat_full = True
                if self._check_nutrient_full(need_nutrient["carbohydrate"], carbohydrate_buff, current_meal_nutrient["carbohydrate"]):
                    self._carbohydrate_full = True
            return False
        return True

    def _check_nutrient_full(self, need_nutrient, buff, current_meal_nutrient):
        if need_nutrient * buff < current_meal_nutrient:
            return True
        return False