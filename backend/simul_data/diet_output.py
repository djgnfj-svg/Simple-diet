import json
import random
import requests

# Open the JSON file for reading
with open('meal_output.json', 'r') as f:
    data = json.load(f)

# Define the values to be added
diet_status_choices = [True, False]
meal_count_choices = [1, 2, 3]

url = 'http://127.0.0.1:8000/api/managing-det/'
headers = {'Content-type': 'application/json'}
for key, value in data.items():
    # Add the new values to the dictionary entry
    value['diet_status'] = random.choice(diet_status_choices)
    value['meal_count'] = random.choice(meal_count_choices)


    response = requests.post(url, headers=headers, data=json.dumps(data))
with open('diet_output.json', 'w') as f:
    json.dump(data, f)

