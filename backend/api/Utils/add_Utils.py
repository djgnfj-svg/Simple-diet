from api.Utils.set_Utils import set_meal_food_data, set_meal_nutrient_data


def add_food_data(meal_food_data, food_data, meal_nutrient_data, food_count, food_double:bool):
    double_value = 1
    if food_double:
        double_value = 2
    # 2-1 대용량
    big_size = 1
    food_number = 1
    if food_data.food_gram > 500:
        if food_data.food_gram > 800:
            big_size = 3
            food_number = 0.3
        else:
            big_size = 2
            food_number = 0.5
    meal_food_data[str(food_count)] = set_meal_food_data(food_data, big_size, food_number, double_value)
    set_meal_nutrient_data(meal_nutrient_data, food_data, big_size, double_value)
