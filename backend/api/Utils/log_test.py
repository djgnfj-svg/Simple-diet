# if i == 0:
#     print_diet(breakfast,meals_data[meals_list[i]], meals_list[i])
# elif i == 1:
#     print_diet(lunch,meals_data[meals_list[i]], meals_list[i])
# elif i == 2:
#     print_diet(dinner,meals_data[meals_list[i]], meals_list[i])
def print_diet(diet_data, meals_data, meal):
    print("========결과=======")
    print("칼로리 비교 : {} : {} | 식단데이터 : {}".format(meal, diet_data["kilo_calorie"], meals_data["kcalorie"]))
    print("단백질 비교 : {} : {} | 식단데이터 : {}".format(meal, diet_data["protein"], meals_data["protein"]))
    print("탄수화물 비교 : {} : {} | 식단데이터 : {}".format(meal, diet_data["carbohydrate"], meals_data["carbohydrate"]))
    print("지방 비교 : {} : {} | 식단데이터 : {}".format(meal, diet_data["fat"], meals_data["fat"]))
    print("==================")

def print_nutrient(diet_data, meals_data, buffer):
    print("단백질 : ",diet_data["protein"] * buffer," ", meals_data["protein"])
    print("탄수화물 : ",diet_data["carbohydrate"] * buffer," ", meals_data["carbohydrate"])
    print("지방 : ",diet_data["fat"] * buffer," ", meals_data["fat"])
