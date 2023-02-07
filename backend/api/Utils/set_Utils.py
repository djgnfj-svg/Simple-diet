def set_meal_nutrient_data(meal_nutrient_data, food_data, big_size, double_value):
    meal_nutrient_data["kcalorie"] += round(food_data.kcalorie / big_size) * double_value
    meal_nutrient_data["protein"] += round(food_data.protein / big_size) * double_value
    meal_nutrient_data["carbohydrate"] += round(food_data.carbohydrate /big_size) * double_value
    meal_nutrient_data["fat"] += round(food_data.fat / big_size,1 ) * double_value

def set_meal_food_data(food_data, big_size, food_number, double_value):
    instance = {}
    instance["food_name"] = food_data.name
    instance["food_link"] = food_data.link
    instance["kcalorie"] = round(food_data.kcalorie /big_size) * double_value
    instance["protein"] = round(food_data.protein/big_size)  * double_value
    instance["fat"] = round(food_data.fat/big_size)  * double_value
    instance["carbohydrate"] = round(food_data.carbohydrate/big_size)  * double_value
    instance["food_number"] = food_number * double_value
    return instance