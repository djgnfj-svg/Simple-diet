from foods.models import Food_data

from api.Utils.log_test import print_diet


def check_data(breakfast_data, meals_data, sort_num):
    buffer = 0.7
    if breakfast_data["protein"] * buffer < meals_data["protein"] and sort_num == 0:
        return 1
    elif breakfast_data["fat"] * buffer< meals_data["fat"] and sort_num==1:
        return 2
    elif breakfast_data["carbohydrate"] * buffer< meals_data["carbohydrate"] and sort_num==2:
        return 10

    return sort_num

# todo 로직 나누기
def init_meals_data(i, meals_list):
    meals_data = {}
    meals_data[meals_list[i]] = {}
    meals_data[meals_list[i]]["kcalorie"] = 0
    meals_data[meals_list[i]]["protein"] = 0
    meals_data[meals_list[i]]["carbohydrate"] = 0
    meals_data[meals_list[i]]["fat"] = 0
    return meals_data

def append_food_data(meal_food_data, food_data, food_count):
    #2 음식 추가    
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
    meal_food_data[str(food_count)]["food_number"] = food_number
    return big_size

#meals = 끼니
#diet = 식단
def Make_week_food_data(total_data, breakfast, lunch, dinner):
    day_food_data = {}
    meals_list = ["breakfast", "lunch", "dinner"]
    sort_list = ["-protein", "-fat", "-carbohydrate"]

    for i in range(0, 3):
        meals_data = init_meals_data(i, meals_list)
        sort_num = 0 
        meal_food_data = {}
        food_count = 0
        
        j = 0
        while True :
            food_datas = Food_data.objects.filter(meals_fucus__icontains = i).order_by(sort_list[sort_num])
            food_data = food_datas[j]

            # 2. 음식 추가여부 확인
            # todo 좀더 우아하게...
            temp = sort_num
            sort_num = check_data(breakfast, meals_data[meals_list[i]], sort_num)

            if sort_num == 10:
                break
            elif temp != sort_num:
                j = 0
                continue
            j += 1
            # 3. 음식추가
            food_count += 1
            big_size = append_food_data(meal_food_data, food_data, food_count)
            meals_data[meals_list[i]]["kcalorie"] += round(food_data.kcalorie / big_size)
            meals_data[meals_list[i]]["protein"] += round(food_data.protein / big_size)
            meals_data[meals_list[i]]["carbohydrate"] += round(food_data.carbohydrate /big_size)
            meals_data[meals_list[i]]["fat"] += round(food_data.fat / big_size)
        day_food_data[meals_list[i]] = meal_food_data
    return day_food_data