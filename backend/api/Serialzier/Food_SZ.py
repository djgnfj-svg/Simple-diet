from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from foods.models import Food_data

NUTRIENT=(
    ('P', '단백질'),
    ('F', '지방'),
    ('C', '탄수화물'),
)

MEALS = (
    ((0), "아침"),
    ((1), "점심"),
    ((2), "저녁"),
    ((0,1), "아침, 점심"),
    ((0,2), "아침, 저녁"),
    ((1,2), "점심, 저녁"),
    ((0,1,2), "전부"),
)


class Food_SZ(serializers.ModelSerializer):
    meals_fucus = serializers.ChoiceField(choices=MEALS)
    nutrient_fucus = serializers.ChoiceField(choices=NUTRIENT)

    name = serializers.CharField(max_length=50)
    kcalorie = serializers.IntegerField(default=0)
    carbohydrate = serializers.FloatField(default=0)
    protein = serializers.FloatField(default=0)
    fat = serializers.FloatField(default=0)
    price = serializers.IntegerField()
    link = serializers.URLField(max_length=200)

    food_number = serializers.IntegerField()
    food_gram = serializers.IntegerField()
    
    class Meta:
        model = Food_data
        fields = "__all__"

    # def validate_meals_fucus(self, values):
    #     for value in values:
    #         if value not in MEALS:
    #             ValidationError("입력데이터가 잘못되었습니다.")
    #     return values

    def create(self, validated_data):
        
        return super().create(validated_data)
    def validate_meals_fucus(self, value):
        if isinstance(value, int):
            return [value]
        return value