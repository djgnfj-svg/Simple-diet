from foods.models import Food_data


def check_data(breakfast_data, meals_data, sort_num):
    # todo 버퍼를 챙겨서 점심데이터로 넘기기
    buffer = 0.7
    # if breakfast_data.kcalorie * buffer < meals_data["kcalorie"]:
    #     return False
    print("단백질 : ",breakfast_data["protein"] * buffer," ", meals_data["protein"])
    print("탄수화물 : ",breakfast_data["carbohydrate"] * buffer," ", meals_data["carbohydrate"])
    print("지방 : ",breakfast_data["fat"] * buffer," ", meals_data["fat"])
    if breakfast_data["protein"] * buffer < meals_data["protein"] and sort_num == 0:
        print("단백질 졸업")
        return 1
    elif breakfast_data["fat"] * buffer< meals_data["fat"] and sort_num==1:
        print("지방 졸업")
        return 2
    elif breakfast_data["carbohydrate"] * buffer< meals_data["carbohydrate"] and sort_num==2:
        print("탄수화물 졸업")
        return 10

    return sort_num

# todo 로직 나누기
def init_meals_data(i):
    meals_data = {}
    meals_data["meals"+str(i)] = {}
    meals_data["meals"+str(i)]["kcalorie"] = 0
    meals_data["meals"+str(i)]["protein"] = 0
    meals_data["meals"+str(i)]["carbohydrate"] = 0
    meals_data["meals"+str(i)]["fat"] = 0
    return meals_data

def append_food_data(i, meal_food_data, food_data, food_count):
    #2 음식 추가
    # 만약 meals_food_data 에 동일한 것이 있다면 푸드넘버만 증가
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
    meal_food_data[str(food_count)]["food_food_number"] = food_number

    return big_size
    
def Make_week_food_data(total_data, breakfast, lunch, dinner):
    day_food_data = {}
    meals_list = ["breakfast", "lunch", "dinner"]
    sort_list = ["-protein", "-fat", "-carbohydrate"]
    nutrient_fucus_list = ["P", "F", "C"]
    for i in range(0, 1):
        meals_data = init_meals_data(i)

        # 1. 어떤 음식을 넣을 껀지에 관한로직
        j = 0
        sort_num = 0        # 탄단지 우선순위 리스트
        meal_food_data = {} #끼니 데이터
        food_count = 0
        print("-------{}---------".format(meals_list[i]))
        while True :
            food_datas = Food_data.objects.filter(meals_fucus__icontains = i).order_by(sort_list[sort_num])
            food_data = food_datas[j]
            # 2. 음식추가
            big_size = append_food_data(i,meal_food_data, food_data, food_count)
            food_count += 1

            # 3. 음식 추가여부 확인
            # todo 원래라면 여기서 버퍼가 작동해야할거같다.
            # 졸업여부확인해서 패스
            # if check_영양소 :
            meals_data["meals"+str(i)]["kcalorie"] += food_data.kcalorie / big_size
            meals_data["meals"+str(i)]["protein"] += food_data.protein / big_size
            meals_data["meals"+str(i)]["carbohydrate"] += food_data.carbohydrate /big_size 
            meals_data["meals"+str(i)]["fat"] += food_data.fat / big_size

            print("음식 이름 : {}".format(food_data.name))
            print("음식 영양소 탄 : {} 단 : {} 지 : {}".format(food_data.carbohydrate,food_data.protein,food_data.fat))
            temp = sort_num
            sort_num = check_data(breakfast, meals_data["meals"+str(i)], sort_num)
            print("----------------------------")
            if sort_num == 10:
                break
            elif temp != sort_num:
                j = 0
            else :
                j += 1
            

        day_food_data[str(meals_list[i])] = meal_food_data
        print("-------{}end---------".format(meals_list[i]))
    return day_food_data