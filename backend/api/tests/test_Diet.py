from rest_framework.test import APITestCase
from rest_framework import status

from api.Utils.msg_utils import test_msg


# 식단 제작 테스트
class DietTest(APITestCase):
    fixtures = ['_master_data/foods-data.json']
    def setUp(self) -> None:
        self.buffer = 0.5
        self.url = "/api/managing-diet/"
        self.sample_data = {
            "total_kcalorie": 3151,
            "total_protein": 176,
            "total_fat": 98,
            "total_carbohydrate": 391,

            "diet_status" : True,
            "meal_count" : 3
        }
        return super().setUp()

    def test_managing_diet(self):
        # Make a GET request to the API endpoint
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_diet_nutrient(self):
        response = self.client.post(self.url, self.sample_data, format="json")
        data = response.data
        meal_breakfast_nutrient = data["breakfast"]["nutrient"]
        need_breakfast_nutrient = data["need_nutrient"]["breakfast"]
        self.assertTrue(self._compare_nutrients(meal_breakfast_nutrient, need_breakfast_nutrient))

        meal_lunch_nutrient = data["lunch"]["nutrient"]
        need_lunch_nutrient = data["need_nutrient"]["lunch"]
        self.assertTrue(self._compare_nutrients(meal_lunch_nutrient, need_lunch_nutrient))

        meal_dinner_nutrient = data["dinner"]["nutrient"]
        need_dinner_nutrient = data["need_nutrient"]["dinner"]
        self.assertTrue(self._compare_nutrients(meal_dinner_nutrient, need_dinner_nutrient))

    def test_print_json_filed(self):
        response = self.client.post(self.url, self.sample_data, format="json")
        #기본 출력확인
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


    def _compare_nutrients(self, meal_nutrient, need_nutrient):
        self.assertTrue(self._conpare_nutrient_value(meal_nutrient["kcalorie"], 
        need_nutrient["kcalorie"]),msg=test_msg(0))

        self.assertTrue(self._conpare_nutrient_value(meal_nutrient["protein"], 
        need_nutrient["protein"]),msg=test_msg(1))
        
        self.assertTrue(self._conpare_nutrient_value(meal_nutrient["fat"], 
        need_nutrient["fat"]),msg=test_msg(2))

        self.assertTrue(self._conpare_nutrient_value(meal_nutrient["carbohydrate"], 
        need_nutrient["carbohydrate"]),msg=test_msg(3))
        return True

    def _conpare_nutrient_value(self, meal, need):
        up_value = (meal + (meal * self.buffer)) 
        down_value = (meal - (meal * self.buffer))
        if (down_value < need < up_value):
            return True
        return False