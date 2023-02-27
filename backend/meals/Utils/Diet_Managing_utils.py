from foods.models import Food

from meals.Utils.Manager import Food_Manager, Meal_Manager


class Diet_Manager(Food_Manager, Meal_Manager):
    def __init__(self, breakfast, lunch, dinner) -> None:
        self._nutrient_list = ["protein", "fat", "carbohydrate"]
        # 영양소 체크

        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

        # 버퍼
        self._food_double_buffer = 2.0
        self._food_over_buffer = 1.3
        self._food_full_buffer = 0.7
        # 2끼라면
        if breakfast == None:
            self._meal_list = ["lunch", "dinner"]
            self._meal_data_list = [lunch, dinner]
            self._start_meal = 0
        # 3끼라면
        else:
            self._meal_list = ["breakfast", "lunch", "dinner"]
            self._meal_data_list = [breakfast, lunch, dinner]
            self._start_meal = 1
        super().__init__()

    def _check_food_over_nutrient(self, food: Food, meal, meal_nutrient_data):
        '''
        음식을 추가했을시 너무 높게 초과된다면 다음 음식을 추가한다.
        현재영양소 + 추가할 음식 영양소 > 채워야하는 영양소 * 버퍼
        '''
        # 채워야 하는 영양소
        if meal == "breakfast":
            nutrient_data = self.breakfast
        elif meal == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        # 채워야하는 영양소 확인
        temp = meal_nutrient_data[meal]
        if not self._protein_full:
            return food.protein + temp["protein"] > \
                nutrient_data["protein"] * self._food_over_buffer
        elif not self._fat_full:
            return food.fat + temp["fat"] > \
                nutrient_data["fat"] * self._food_over_buffer
        elif not self._carbohydrate_full:
            return food.carbohydrate + temp["carbohydrate"] > \
                nutrient_data["carbohydrate"] * self._food_over_buffer
        return False

    # todo : 간단한 음식인가에 대한 여부도 체크해야한다.~
    def _check_food_double(self, food: Food, meal, meal_nutrient_data):
        '''
        음식영양소 * 버퍼, < 목표영양소 - 현재영양소
        '''
        if meal == "breakfast":
            nutrient_data = self.breakfast
        elif meal == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        temp = meal_nutrient_data[meal]
        # todo big_size일 경우 처리가 안됨
        if not self._protein_full:
            return food.protein * self._food_double_buffer < \
                nutrient_data["protein"] - temp["protein"]
        elif not self._fat_full:
            return food.fat * self._food_double_buffer < \
                nutrient_data["fat"] - temp["fat"]
        elif not self._carbohydrate_full:
            return food.carbohydrate * self._food_double_buffer < \
                nutrient_data["carbohydrate"] - \
                temp["carbohydrate"]
        else:
            self._check_nutrient_full = True
        return False

    def _check_nutrient(self, meal, meal_nutrient_data, food_focus):
        '''
        채워야하는양 * 버퍼 < 현재 채워진양  
        '''
        # todo : 함수화 해야됨
        if meal == "breakfast":
            nutrient_data = self.breakfast
        elif meal == "lunch":
            nutrient_data = self.lunch
        else:
            nutrient_data = self.dinner

        temp = meal_nutrient_data[meal]
        if nutrient_data["protein"] * self._food_full_buffer < temp["protein"] and not self._protein_full:
            self._protein_full = True
            return 0
        elif nutrient_data["fat"] * self._food_full_buffer < temp["fat"] and not self._fat_full:
            self._fat_full = True
            return 0
        elif nutrient_data["carbohydrate"] * self._food_full_buffer < temp["carbohydrate"]:
            self._carbohydrate_full = True
            self._check_nutrient_full = True
            return 0
        return food_focus+1  # todo : 여기서 0이 리턴되는 것도 문제이다.

    def _set_meal_nutrient_data(self, meal_nutrient_data, food_data, big_size, double_value):
        meal_nutrient_data["kcalorie"] += round(food_data.kcalorie / big_size) * double_value
        meal_nutrient_data["protein"] += round(food_data.protein / big_size) * double_value
        meal_nutrient_data["fat"] += round(food_data.fat /big_size) * double_value 
        meal_nutrient_data["carbohydrate"] += round(food_data.carbohydrate / big_size) * double_value

    def _add_meal_food_data(self, meal_food_data, meal_nutrient_data, food: Food,
                            meal, food_count, food_double):
        double_value = 2 if food_double else 1
        big_size = 1
        food_number = 1
        if food.food_gram > 500:
            self._meal_have_bigsize_food = True
            if food.food_gram > 800:
                big_size = 3
                food_number = 0.3
            else:
                big_size = 2
                food_number = 0.5

        meal_food_data[str(food_count)] = self._set_meal_food_data(food, big_size, food_number, double_value)
        self._set_meal_nutrient_data(meal_nutrient_data[meal], food, big_size, double_value)
    # 식단 정보 데이타

    def get_diet_info(self):
        diet_info = {}
        for _, meal in enumerate(self._meal_list):
            #     # 이번 식사의 음식
            meal_food_data = {}
            self._protein_full = False
            self._fat_full = False
            self._carbohydrate_full = False
            self._check_nutrient_full = False
            # 이번 식사에서 먹어야 영양소의양
            meal_nutrient_data = {}
            meal_nutrient_data[meal] = self._init_meal_nutrient_data()

            # 대용량 음식여부(식단마다 대용량은 하나만 가능하다.)
            self._meal_have_bigsize_food = False
            # 단 -> 지 -> 탄순으로 채울떄까지 반복한다.
            food_count = 0
            food_focus = 0
            # todo : 현재 food_count가 초기화되면서 0번음식이 덮어쓰여지는 문제가 있다.
            while not self._check_nutrient_full:
                # todo : foods로 받은이후 food_count가 0이 아니면 건너 뛰어도 상관없다
                food = self._get_food(meal, food_focus)

                # bigsize 음식은 식사에서 한개만 챙긴다.
                if food.food_gram > 500 and self._meal_have_bigsize_food:
                    food_focus += 1
                    continue
                # 지금 음식을 넣으면 영양소가 넘치나?
                if self._check_food_over_nutrient(food, meal, meal_nutrient_data):
                    food_focus += 1
                    continue
                food_double = self._check_food_double(food, meal, meal_nutrient_data)

                # 현재음식을 추가
                # 현재여기 무넺임
                meal_food_data[str(food_count)] = self._init_meal_nutrient_data()
                self._add_meal_food_data(meal_food_data, meal_nutrient_data, food, meal, food_count, food_double)
                food_count += 1
                food_focus = self._check_nutrient(meal, meal_nutrient_data, food_focus)

            # 영양소를 만족한 식단을 diet_info에 추가한다.
            diet_info[meal] = meal_food_data
            diet_info[meal]["nutrient"] = meal_nutrient_data[meal]
        return diet_info
