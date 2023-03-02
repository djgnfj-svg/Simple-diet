from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import ErrorDetail
# 테스트 할 목록
# 기초대사량테스트
# 추후 코드를 리팩토링 할떄 용의하게 사용하기 위해서
# 1.


class DietCalutationsTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/calc_metabolic/'
        self.body_info = {
            "age": 25,
            "weight": 110,
            "height": 173,

            "gender": "M",
            "general_activities": 1.2,
            "excise_activity": 0.2,

        }
        return super().setUp()
    # 테스트할 목록
    # 결과가 옳케 나오나
    # 에러가 옳케 나오나
    # 그정도네

    def test_api_cal_returns_expected_data(self):
        expected_response = {
                "total_kcalorie": 3151,
                "total_protein": 176,
                "total_fat": 98,
                "total_carbohydrate": 391
        }
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)
    
    def test_api_cal_returns_error_msg_age(self):
        expected_response_over_age = {'error_msg': {'age': [ErrorDetail(string='Ensure this value is less than or equal to 100.', code='max_value')]}}
        expected_response_under_age = {'error_msg': {'age': [ErrorDetail(string='Ensure this value is greater than or equal to 20.', code='min_value')]}}

        self.body_info["age"] = 9999
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_over_age)

        self.body_info["age"] = 5
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_under_age)
    
    def test_api_cal_returns_error_msg_weight(self):
        expected_response_over_weight = {'error_msg': {'weight': [ErrorDetail(string='Ensure this value is less than or equal to 250.', code='max_value')]}}
        expected_response_under_weight = {'error_msg': {'weight': [ErrorDetail(string='Ensure this value is greater than or equal to 40.', code='min_value')]}}

        self.body_info["weight"] = 9999
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_over_weight)

        self.body_info["weight"] = 5
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_under_weight)
    
    def test_api_cal_returns_error_msg_height(self):
        expected_response_over_height = {'error_msg': {'height': [ErrorDetail(string='Ensure this value is less than or equal to 250.', code='max_value')]}}
        expected_response_under_height = {'error_msg': {'height': [ErrorDetail(string='Ensure this value is greater than or equal to 140.', code='min_value')]}}

        self.body_info["height"] = 9999
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_over_height)

        self.body_info["height"] = 5
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_under_height)

    def test_api_cal_returns_error_msg_gender(self):
        expected_response_wrong_gender = {'error_msg': {'gender': [ErrorDetail(string='"A" is not a valid choice.', code='invalid_choice')]}}
        expected_response_None_gender = {'error_msg': {'gender': [ErrorDetail(string='This field may not be null.', code='null')]}}

        self.body_info["gender"] = "A"
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_wrong_gender)

        self.body_info["gender"] = None
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_None_gender)

    def test_api_cal_returns_error_msg_general_activities(self):
        expected_response_over_general_activities = {'error_msg': {'general_activities': [ErrorDetail(string='Ensure this value is less than or equal to 1.6.', code='max_value')]}}
        expected_response_under_general_activities = {'error_msg': {'general_activities': [ErrorDetail(string='Ensure this value is greater than or equal to 1.2.', code='min_value')]}}

        self.body_info["general_activities"] = 3.0
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_over_general_activities)

        self.body_info["general_activities"] = 0.1
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_under_general_activities)

    def test_api_cal_returns_error_msg_excise_activity(self):
        expected_response_over_excise_activity = {'error_msg': {'excise_activity': [ErrorDetail(string='Ensure this value is less than or equal to 0.3.', code='max_value')]}}
        expected_response_None_excise_activity = {'error_msg': {'excise_activity': [ErrorDetail(string='This field may not be null.', code='null')]}}

        self.body_info["excise_activity"] = 2.0
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_over_excise_activity)

        self.body_info["excise_activity"] = None
        response = self.client.post(self.url, self.body_info, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_None_excise_activity)
    
        