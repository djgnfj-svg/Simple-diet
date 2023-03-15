from foods.models import Food

from meals.Utils.Food_Manager import Food_Manager


class Meals_Assign:
    def __init__(self, diet_custom_data) -> None:
        _diet_cut = 0.8 if diet_custom_data["diet_status"] else 1
        self._assign_total_data(_diet_cut, diet_custom_data)

        if diet_custom_data["meal_count"] == 3:
            self._meal_ratio = [0.25, 0.45, 0.3]
            self._meal_list = ["breakfast", "lunch", "dinner"]
        elif diet_custom_data["meal_count"] == 2:
            self._meal_ratio = [0.6, 0.4]
            self._meal_list = ["breakfast", "lunch"]
        else:
            self._meal_ratio = [1]
            self._meal_list = ["breakfast"]

        self._assign_meals_nutrient()

    def _assign_total_data(self, diet_cut, diet_custom_data):
        self.total_kcalorie = diet_custom_data["total_kcalorie"] * diet_cut
        self.total_protein = diet_custom_data["total_protein"] * diet_cut
        self.total_fat = diet_custom_data["total_fat"] * diet_cut
        self.total_carbohydrate = diet_custom_data["total_carbohydrate"] * diet_cut

    def _assign_meals_nutrient(self):
        self.meals = {}
        for i, meal in enumerate(self._meal_list):
            self.meals[meal] = {}
            self.meals[meal]["kcalorie"] = round(
                self.total_kcalorie * self._meal_ratio[i])
            self.meals[meal]["protein"] = round(
                self.total_protein * self._meal_ratio[i])
            self.meals[meal]["fat"] = round(
                self.total_fat * self._meal_ratio[i])
            self.meals[meal]["carbohydrate"] = round(
                self.total_carbohydrate * self._meal_ratio[i])

    def get_meal(self, meal):
        return self.meals[meal]


class Meal_Calculation(Meals_Assign, Food_Manager):
    def __init__(self, diet_custom_data) -> None:
        Meals_Assign.__init__(self, diet_custom_data)
        Food_Manager.__init__(self)

        if diet_custom_data["meal_count"] == 3:
            self.breakfast_need_nutrient = self.meals["breakfast"]
            self.lunch_need_nutrient = self.meals["lunch"]
            self.dinner_need_nutrient = self.meals["dinner"]

        elif diet_custom_data["meal_count"] == 2:
            self.breakfast_need_nutrient = self.meals["breakfast"]
            self.lunch_need_nutrient = self.meals["lunch"]
        else:
            self.breakfast_need_nutrient = self.meals["breakfast"]

    def _add_meal_food_data(self, meal_food_data, current_meal_nutrient, food: Food,
                            meal_name, food_count, isdouble):

        double_value = 2 if isdouble else 1
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

        meal_food_data[str(food_count)] = self._assign_meal_food_data(
            food, big_size, food_number, double_value)

        self._assign_food_nutrient(
            current_meal_nutrient[meal_name], food, big_size, double_value)

    def calc_meal(self, protein_buff, fat_buff, carbohydrate_buff):
        diet_info = {}
        for _, meal_name in enumerate(self._meal_list):
            meal_food_data = {}
            self._protein_full = False
            self._fat_full = False
            self._carbohydrate_full = False
            self._meal_have_bigsize_food = False

            current_meal_nutrient = {}
            current_meal_nutrient[meal_name] = self._init_nutrient()

            food_count = 0
            food_focus = 0
            while not self._carbohydrate_full:
                food = self._get_food(meal_name, food_focus)
                if (food.food_gram > 500 and self._meal_have_bigsize_food):
                    food_focus += 1
                    continue
                
                if self._check_food_over_nutrient(food, meal_name, current_meal_nutrient):
                    food_focus += 1
                    continue

                food_double = self._check_food_double(
                    food, meal_name, current_meal_nutrient)
                meal_food_data[str(food_count)] = self._init_nutrient()
                self._add_meal_food_data(meal_food_data, current_meal_nutrient, food, meal_name, food_count, food_double)
                food_count += 1
                if not self._check_nutrient_all_full(meal_name, current_meal_nutrient[meal_name],
                                             protein_buff, fat_buff, carbohydrate_buff):
                    food_focus = 0
            diet_info[meal_name] = meal_food_data
            diet_info[meal_name]["nutrient"] = current_meal_nutrient[meal_name]
        return diet_info
