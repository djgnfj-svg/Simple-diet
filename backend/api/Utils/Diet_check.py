def check_food_double(food_data, nutrient_data, meal_food_data, sort_num):
    buffer = 2.0
    if sort_num == 0:
        return food_data.protein * buffer < nutrient_data["protein"] - meal_food_data
    elif sort_num == 1:
        return food_data.fat * buffer < nutrient_data["fat"] - meal_food_data
    return food_data.carbohydrate * buffer < nutrient_data["carbohydrate"] - meal_food_data

def check_nutrient(nutrient_data, meals_data, sort_num):
    buffer = 0.7
    if nutrient_data["protein"] * buffer < meals_data["protein"] and sort_num == 0:
        return 1
    elif nutrient_data["fat"] * buffer< meals_data["fat"] and sort_num==1:
        return 2
    elif nutrient_data["carbohydrate"] * buffer< meals_data["carbohydrate"] and sort_num==2:
        return 10
    return sort_num

def check_food_data(meal_food_data, food_data, nutrient_data, sort_num):
    buffer = 1.3
    if sort_num == 0:
        return meal_food_data + food_data.protein > nutrient_data["protein"] * buffer
    elif sort_num == 1:
        return meal_food_data + food_data.fat > nutrient_data["fat"] * buffer
    return meal_food_data + food_data.carbohydrate > nutrient_data["carbohydrate"] * buffer