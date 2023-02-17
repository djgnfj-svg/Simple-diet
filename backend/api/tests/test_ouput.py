from rest_framework import status
from rest_framework.test import APITestCase

# class MyApiViewTestCase(APITestCase):

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