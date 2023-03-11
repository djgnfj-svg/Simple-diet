from rest_framework.test import APITestCase

# UI 테스트
class metabolic_diet_UI_TestCase(APITestCase):
    fixtures = ['_master_data/food-Category.json', '_master_data/foods-data.json',]
    def setUp(self) -> None:
        self.metabolic_url = '/api/calc-metabolic/'
        self.body_info = {
            "age": 25,
            "weight": 100,
            "height": 173,

            "gender": "M",
            "general_activities": 1.2,
            "excise_activity": 0.0,
        }

        self.diet_url = "/api/managing-diet/"
        self.diet_custom = {
            "diet_status" : True,
            "meal_count" : 3 
        }
        return super().setUp()
    
    def test_main_root(self):
        response = self.client.post(self.metabolic_url, self.body_info, format='json')

        diet_custom_data = response.data
        diet_custom_data["diet_status"] = self.diet_custom["diet_status"]
        diet_custom_data["meal_count"] = self.diet_custom["meal_count"]

        response = self.client.post(self.diet_url, diet_custom_data, format="json")

        #기본 출력 확인
        self.assertIn('breakfast', response.data)
        self.assertIn('lunch', response.data)
        self.assertIn('dinner', response.data)
        self.assertIn('need_nutrient', response.data)
        
        #필요 영양소 출력 테스트
        need_nutrient_data = response.data["need_nutrient"]
        self.assertIn("breakfast", need_nutrient_data)
        self.assertIn("lunch", need_nutrient_data)
        self.assertIn("dinner", need_nutrient_data)

        # breakfast
        breakfast_data = response.data["breakfast"]
        self.assertIn('nutrient', breakfast_data)
        self.assertIn('0', breakfast_data)

        breakfast_nutrient_data = breakfast_data["nutrient"]
        self.assertIn("kcalorie", breakfast_nutrient_data)
        self.assertIn("protein", breakfast_nutrient_data)
        self.assertIn("fat", breakfast_nutrient_data)
        self.assertIn("carbohydrate", breakfast_nutrient_data)

        #lunch
        lunch_data = response.data["lunch"]
        self.assertIn('nutrient', lunch_data)
        self.assertIn('0', lunch_data)

        lunch_nutrient_data = lunch_data["nutrient"]
        self.assertIn("kcalorie", lunch_nutrient_data)
        self.assertIn("protein", lunch_nutrient_data)
        self.assertIn("fat", lunch_nutrient_data)
        self.assertIn("carbohydrate", lunch_nutrient_data)
        
        # diner
        dinner_data = response.data["dinner"]
        self.assertIn('nutrient', dinner_data)
        self.assertIn('0', dinner_data)

        dinner_nutrient_data = dinner_data["nutrient"]
        self.assertIn("kcalorie", dinner_nutrient_data)
        self.assertIn("protein", dinner_nutrient_data)
        self.assertIn("fat", dinner_nutrient_data)
        self.assertIn("carbohydrate", dinner_nutrient_data)


