from rest_framework import status
from rest_framework.test import APITestCase
from api.tests.manager_sample_data import BODY_INFO_DATA
from foods.models import Food_Categories, Food


global over_range
global food_count
class Nutrient_ManagerTestCase(APITestCase):
    # 식단을 만든다.
        # 식단을 만들기 위한 body_info의 샘플데이터를 만든다.
        # 결과가 나왔을때 
    # 매니져가 생성되었는지 확인한다.
    # 음식을 추가한다
    # 음식을 추가할떄도 매니져가 쿰쩍되는지 확인한다.
    
    fixtures = ['_master_data/foods-data.json']
    def setUp(self):
        self.basal_metabolic_rate_url = '/api/cal-diet/'
        self.diet_managing_url = "/api/managing-diet/"
        self.food_url =  "/api/food/"

        self.aver = 0
        self.category = Food_Categories.objects.create(name='Test Category')
        self.food_data = {
            'name': 'Test Food',
            'link': 'https://www.example.com/test-food',
            'category': {"name" : self.category.name},
            'meals_fucus': "(0, 1)",
            'kcalorie': 100,
            'protein': 1.5,
            'fat': 5.0,
            'carbohydrate': 1.5,
            'food_number': 1,
            'food_gram': 100,
        }
        self.sample_body_info_datas = BODY_INFO_DATA
    
    # 식품이 얼마나 오버하는지 알고 싶을때 사용
    def test_over_nutrient(self):
        count = 0
        for i in BODY_INFO_DATA:
            basal_metabolic_rate_data = self.client.post(self.basal_metabolic_rate_url, BODY_INFO_DATA[i], format='json')
            diet_data = {"data" : basal_metabolic_rate_data.data}
            response = self.client.post(self.diet_managing_url, diet_data, format="json")
            if self.check_over_nutrient(response.data, i+1):
                count += 1


    def check_over_nutrient(self,response, body_info_count):
        meal_list = ["breakfast", "lunch", "dinner"]
        for i in meal_list:
            try:
                need = response[i+"_nutrient"]
                meal = response[i]["nutrient"]
            except KeyError :
                pass
            else:
                if need["protein"] + need["protein"] * 0.1 < meal["protein"]:
                    new_value = (meal["protein"] - need["protein"]) / need["protein"] * 100
                    self.aver = self.calk_aver(self.aver, new_value, body_info_count)
                    return True
                elif need["fat"] + need["fat"]* 0.1 < meal["fat"]:
                    new_value = (meal["fat"] - need["fat"]) / need["fat"] * 100
                    self.aver = self.calk_aver(self.aver, new_value, body_info_count)
                    return True
                elif need["carbohydrate"] + need["carbohydrate"]* 0.1 < meal["carbohydrate"]:
                    new_value = (meal["carbohydrate"] - need["carbohydrate"]) / need["carbohydrate"] * 100
                    self.aver = self.calk_aver(self.aver, new_value, body_info_count)
                    return True
        return False


    def calk_aver(self, preaver, new_value, food_len):
        old_weight = (food_len - 1) / food_len
        new_weight = 1 / food_len
        food_len += 1
        return (preaver * old_weight) + (new_value * new_weight)
