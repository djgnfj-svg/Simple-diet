from rest_framework import serializers

from api.Serialzier.Food_Categories_SZ import Food_Categories_SZ

from foods.models import Food_data

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
    # 기본 정보
    name = serializers.CharField(max_length=50)
    link = serializers.URLField(max_length=200)
    # category = Food_Categories_SZ(read_only=True)

    # 영양소 정보
    kcalorie = serializers.IntegerField(default=0)
    carbohydrate = serializers.FloatField(default=0)
    protein = serializers.FloatField(default=0)
    fat = serializers.FloatField(default=0)

    # 끼니별 정보
    food_number = serializers.IntegerField()
    food_gram = serializers.IntegerField()
    
    meals_fucus = serializers.ChoiceField(choices=MEALS)

    class Meta:
        model = Food_data
        # exclude = ["id"]
        fields = '__all__'

    def validate_meals_fucus(self, value):
        print(f"여긴가 {type(value)}")
        if isinstance(value, int):
            print(type([value]))
            return [value]
        return value