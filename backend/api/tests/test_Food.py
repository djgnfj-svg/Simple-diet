from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from foods.models import Food_Categories, Food

# 음식 테스트
class FoodTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/foods/"
        self.category = Food_Categories.objects.create(name='Test Category')
        self.valid_payload = {
            'name': 'Test Food',
            'link': 'https://www.example.com/test-food',
            'category': {"name" : self.category.name},
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
            'kcalorie': -1,
            'protein': -1,
            'fat': -1,
            'carbohydrate': -1,
            'food_number': -1,
            'food_gram': -1,
        }
        
    def test_create_valid_food_data(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Food.objects.count(), 1)
        self.assertEqual(Food.objects.get().name, 'Test Food')
        self.assertEqual(Food.objects.get().category.name, 'Test Category')

    def test_create_invalid_food_data(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Food.objects.count(), 0)