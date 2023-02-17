import requests
import json
url = 'https://api-gateway.coupang.com/v2/providers/seller_api/apis/api/v1/marketplace/seller-products/{sellerProductId}/partial'

# Replace {sellerProductId} with the actual ID of the seller product

headers = {
    # 'Authorization': f'Bearer <your_access_token>',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

# Set the encoding to UTF-8 when printing the output
print(response.content.decode('utf-8'))