def init_nutrient_data(meals):
    meals_data = {}
    meals_data[meals] = {}
    meals_data[meals]["kcalorie"] = 0
    meals_data[meals]["protein"] = 0
    meals_data[meals]["fat"] = 0
    meals_data[meals]["carbohydrate"] = 0
    return meals_data

def init_meal_food_data():
    instance = {}
    instance["kcalorie"] = 0
    instance["protein"] = 0
    instance["fat"] = 0
    instance["carbohydrate"] = 0
    return instance