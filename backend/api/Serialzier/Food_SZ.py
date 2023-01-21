from rest_framework import serializers

from foods.models import Food_data

NUTRIENT=(
        ('P', '단백질'),
        ('F', '지방'),
        ('C', '탄수화물'),
)

MEALS = (
    (0, "아침"),
    (1, "점심"),
    (2, "저녁"),
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
    food_number = serializers.IntegerField()
    food_gram = serializers.IntegerField()
    link = serializers.URLField(max_length=200)

    
    class Meta:
        model = Food_data
        fields = "__all__"