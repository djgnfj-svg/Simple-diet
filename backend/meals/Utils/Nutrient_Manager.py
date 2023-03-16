class Nutrient_Assign:

    @staticmethod
    def init_nutrient():
        nuturient = {}
        nuturient["kcalorie"] = 0
        nuturient["protein"] = 0
        nuturient["fat"] = 0
        nuturient["carbohydrate"] = 0
        return nuturient
    
class Nutrient_Checker(Nutrient_Assign):
    @staticmethod
    def check_nutrient_full(need_nutrient, buff, current_meal_nutrient):
        if need_nutrient * buff < current_meal_nutrient:
            return True
        return False

class Nutrient_Manager(Nutrient_Checker):
    def __init__(self) -> None:
        super().__init__()
    
