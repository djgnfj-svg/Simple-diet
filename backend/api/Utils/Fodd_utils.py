from foods.models import Food_data

from api.Utils.log_test import print_diet, print_nutrient

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
        print("단백질 졸업")
        return 1
    elif nutrient_data["fat"] * buffer< meals_data["fat"] and sort_num==1:
        print("지방 졸업")
        return 2
    elif nutrient_data["carbohydrate"] * buffer< meals_data["carbohydrate"] and sort_num==2:
        print("탄수화물 졸업")
        return 10
    return sort_num

def check_food_data(meal_food_data, food_data, nutrient_data, sort_num):
    buffer = 1.3
    # 현재값 + 음식값 > 만족값 * 버퍼
    # 음식을 더했을떄 너무 높으면 거르기 위한 로직
    if sort_num == 0:
        return meal_food_data + food_data.protein > nutrient_data["protein"] * buffer
    elif sort_num == 1:
        return meal_food_data + food_data.fat > nutrient_data["fat"] * buffer
    return meal_food_data + food_data.carbohydrate > nutrient_data["carbohydrate"] * buffer


def add_food_data(meal_food_data, food_data, meal_nutrient_data, food_count, food_double:bool):
    double_value = 1
    if food_double:
        double_value = 2
    meal_food_data[str(food_count)] = {}
    meal_food_data[str(food_count)]["food_name"] = food_data.name
    meal_food_data[str(food_count)]["food_link"] = food_data.link
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

    meal_food_data[str(food_count)]["kcalorie"] = round(food_data.kcalorie /big_size) * double_value
    meal_food_data[str(food_count)]["protein"] = round(food_data.protein/big_size)  * double_value
    meal_food_data[str(food_count)]["fat"] = round(food_data.fat/big_size)  * double_value
    meal_food_data[str(food_count)]["carbohydrate"] = round(food_data.carbohydrate/big_size)  * double_value
    meal_food_data[str(food_count)]["food_number"] = food_number * double_value
    meal_nutrient_data["kcalorie"] += round(food_data.kcalorie / big_size) * double_value
    meal_nutrient_data["protein"] += round(food_data.protein / big_size) * double_value
    meal_nutrient_data["carbohydrate"] += round(food_data.carbohydrate /big_size) * double_value
    meal_nutrient_data["fat"] += round(food_data.fat / big_size,1 ) * double_value
    return 


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

def Make_week_food_data(total_data, breakfast, lunch, dinner):
    '''
    목표 : 영양소를 받아서 그것을 만족하는 식단과 식단의 영양소를 리턴

    1. 영양소를 식사별로 나눈다.0
    2. 식사수 만큼 반복문을돈다.0
    3. 탄단지 순서로 만족하도록 반복문을 돈다.0
    4. 음식 리스트를 뽑는다. 0
    5. 식사에 음식을 추가한다.
    6. 더 추가해야하는지 체크한다.
    7. 없다면 3번으로 돌아가고, 탄수화물까지 만족했다면 식사를 저장한다.
    '''
    instance = {}
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
        while True :
            food_datas = Food_data.objects.filter(meals_fucus__icontains = meal).order_by("-"+sort_list[sort_num])
            food_data = food_datas[j]
            food_double = False
            if food_data.food_gram < 500:
                meal_food_data[str(food_count)] = init_meal_food_data()
                try :
                    # str(food_count)가 문제임
                    if check_food_data(meal_food_data[str(food_count)][sort_list[sort_num]], food_data, nutrient_list[meal], sort_num):
                        j += 1
                        continue
                    elif check_food_double(food_data, nutrient_list[meal], meal_food_data[str(food_count)][sort_list[sort_num]], sort_num):
                        food_double = True
                except Exception  as e:
                    print(e)
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