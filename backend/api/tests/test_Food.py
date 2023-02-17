from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from foods.models import Food_Categories, Food_data

# 테스트 할 목록
# 기초대사량테스트
    # 추후 코드를 리팩토링 할떄 용의하게 사용하기 위해서
        # 1. 
# 식단 영양소와 거시기를 비고
    # 10개의 다른 데이터를 비교해서 심하게 넘어가는게 5개 이상이면 막는다.

class FoodTestCase(APITestCase):
    def setUp(self):
        self.category = Food_Categories.objects.create(name='Test Category')
        self.valid_payload = {
            'name': 'Test Food',
            'link': 'https://www.example.com/test-food',
            'category': {"name" : self.category.name},
            'meals_fucus': "(0, 1)",
            'kcalorie': 100,
            'protein': 10.5,
            'fat': 5.0,
            'carbohydrate': 20.5,
            'food_number': 1,
            'food_gram': 100,
        }
        self.invalid_payload = {
            'name': '',
            'link': 'invalid_url',
            'category': '',
            'meals_fucus': 'not_an_array',
            'kcalorie': -1,
            'protein': -1,
            'fat': -1,
            'carbohydrate': -1,
            'food_number': -1,
            'food_gram': -1,
        }
        
    def test_create_valid_food_data(self):
        url = "/api/food/"
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Food_data.objects.count(), 1)
        self.assertEqual(Food_data.objects.get().name, 'Test Food')
        self.assertEqual(Food_data.objects.get().category.name, 'Test Category')

    def test_create_invalid_food_data(self):
        url = "/api/food/"
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Food_data.objects.count(), 0)