from api.Utils.Diet_check import check_food_data, check_food_double, check_nutrient
from api.Utils.init_utils import init_meal_food_data, init_nutrient_data
from api.Utils.add_Utils import add_food_data
from foods.models import Food_data

def Make_week_food_data(total_data, breakfast, lunch, dinner):
    day_food_data = {}
    meal_three = True if breakfast != None else False
    nutrient_list = [breakfast, lunch, dinner]
    meal_list = ["breakfast", "lunch", "dinner"] 
    sort_list = ["protein", "fat", "carbohydrate"]

    start_meal = 0 if meal_three else 1
    for meal in range(start_meal, 3):
        meal_nutrient_data = init_nutrient_data(meal_list[meal])
        meal_food_data = {} # 먹어야하는 음식 데이터
        sort_num = 0        # 단백질, 지방, 탄수화물 순서대로 완료하기 위해서
        j = 0
        food_count = 0
        big_size_food = False
        while True :
            food_data = Food_data.objects.filter(meals_fucus__icontains = meal).order_by("-"+sort_list[sort_num])[j]
            food_double = False
            #big size check
            if food_data.food_gram > 500:
                if not big_size_food:
                    j += 1
                    continue
                big_size_food = True
            meal_food_data[str(food_count)] = init_meal_food_data()
            try :
                if check_food_data(meal_food_data[str(food_count)][sort_list[sort_num]], food_data, nutrient_list[meal], sort_num):
                    j += 1
                    continue
                elif check_food_double(food_data, nutrient_list[meal], meal_food_data[str(food_count)][sort_list[sort_num]], sort_num):
                    food_double = True
            except Exception  as e:
                print(e)

            # 영양소 기준체크(단 지 탄 순으로 전부 채웠다면 패스)
            temp = sort_num
            add_food_data(meal_food_data, food_data, meal_nutrient_data[meal_list[meal]], food_count, food_double)
            food_count += 1
            sort_num = check_nutrient(nutrient_list[meal], meal_nutrient_data[meal_list[meal]], sort_num)
            if sort_num == 10:
                break
            elif temp != sort_num:
                j = 0
                continue
            j += 1
        day_food_data[meal_list[meal]] = meal_food_data
        day_food_data[meal_list[meal]]["nutrient"] = nutrient_list[meal]
    return day_food_data