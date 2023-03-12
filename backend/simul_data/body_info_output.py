import requests
import random
import json

url = 'http://127.0.0.1:8000/api/calc_metabolic/'

# Define the input data ranges
age_range = (20, 50)
weight_range = (50, 100)
height_range = (150, 185)
gender_choices = ('M', 'F')
general_activities_choices = (1.2, 1.4, 1.6)
excise_activity_choices = (0, 0.1, 0.2, 0.3)

# Create 100 sets of random input data
output_data = {}
for i in range(100):
    input_data = {
        'age': random.randint(*age_range),
        'weight': random.randint(*weight_range),
        'height': random.randint(*height_range),
        'gender': random.choice(gender_choices),
        'general_activities': random.choice(general_activities_choices),
        'excise_activity': random.choice(excise_activity_choices)
    }
    
    # Send a POST request with the input data and receive the response in JSON format
    response = requests.post(url, json=input_data, headers={'Content-Type': 'application/json'})
    output_data[i] = response.json()

# Save the output data as a JSON file
with open('meal_output.json', 'w') as f:
    json.dump(output_data, f)
