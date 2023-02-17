from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

# 테스트 할 목록
# 기초대사량테스트
    # 추후 코드를 리팩토링 할떄 용의하게 사용하기 위해서
        # 1. 
# 식단 영양소와 거시기를 비고
    # 10개의 다른 데이터를 비교해서 심하게 넘어가는게 5개 이상이면 막는다.

# class MyApiViewTestCase(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='testuser@test.com',
#             password='testpassword'
#         )
#         self.client.force_authenticate(user=self.user)
#     def test_api_view_returns_expected_data(self):
#         # Setup
#         url = '/api/my-endpoint/'
#         data = {'foo': 'bar'}
#         expected_response = {'foo': 'bar', 'baz': 123}

#         # Make request
#         response = self.client.post(url, data, format='json')

#         # Verify response
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, expected_response)