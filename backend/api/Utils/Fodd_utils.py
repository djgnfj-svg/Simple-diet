from foods.models import Food_data


def check_data(breakfast_data, meals_data):
    # todo 버퍼를 챙겨서 점심데이터로 넘기기
    buffer = 0.9
    # if breakfast_data.kcalorie * buffer < meals_data["kcalorie"]:
    #     return False
    if breakfast_data["protein"] * buffer < meals_data["protein"]:
        return 0
    elif breakfast_data["carbohydrate"] * buffer< meals_data["carbohydrate"]:
        return 1
    elif breakfast_data["fat"] * buffer< meals_data["fat"]:
        return 2

    return 10

def Make_week_food_data(total_data, breakfast, lunch, dinner):
    day_food_data = {}
    meals_list = ["breakfast", "lunch", "dinner"]
    sort_list = ["protein", "fat", "carbohydrate"]
    breakfast_food_data = {}
    for i in range(0, 3):
        diet_data = {}
        diet_data["meals"+str(i)] = {}
        diet_data["meals"+str(i)]["kcalorie"] = 0
        diet_data["meals"+str(i)]["protein"] = 0
        diet_data["meals"+str(i)]["carbohydrate"] = 0
        diet_data["meals"+str(i)]["fat"] = 0

        # 1. 어떤 음식을 넣을 껀지에 관한로직
        # 1-1 3가지로 추리자
        j = 0
        sort_num = 0
        while True : 
            if j > 10:
                return
            food_datas = Food_data.objects.filter(meals_fucus__icontains = i).order_by(sort_list[sort_num])
            food_data = food_datas[j]
            # 2. 음식 추가하기
                # 추가시에 대용량인지 확인하기
            # 총 열량 맞나 체크하기
            # 음식 데이터 추가
            # 위처럼 했을때 출력은
                # food_name food_link food_number
            
            #2 음식 추가
            breakfast_food_data[str(i)] = {}
            breakfast_food_data[str(i)]["food_name"] = food_data.name
            breakfast_food_data[str(i)]["food_link"] = food_data.link
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
            breakfast_food_data[str(i)]["food_food_number"] = food_number

            diet_data["meals"+str(i)]["kcalorie"] += food_data.kcalorie / big_size
            diet_data["meals"+str(i)]["protein"] += food_data.protein / big_size
            diet_data["meals"+str(i)]["carbohydrate"] += food_data.carbohydrate /big_size 
            diet_data["meals"+str(i)]["fat"] += food_data.fat / big_size
            sort_num = check_data(breakfast, diet_data["meals"+str(i)])
            if sort_num == 10:
                print("출소다")
                break
            j += 1
            

        day_food_data[str(meals_list[i])] = breakfast_food_data
    print(type(day_food_data))
    return day_food_data