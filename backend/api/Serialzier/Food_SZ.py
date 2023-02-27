from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.response import Response

from foods.models import Food, Food_Categories

from api.Utils.msg_utils import error_msg
from api.Serialzier.Food_Categories_SZ import Food_Categories_SZ

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

    # 영양소 정보
    kcalorie = serializers.IntegerField(default=0)
    carbohydrate = serializers.FloatField(default=0)
    protein = serializers.FloatField(default=0)
    fat = serializers.FloatField(default=0)

    # 끼니별 정보
    food_number = serializers.IntegerField()
    food_gram = serializers.IntegerField()
    
    meals_fucus = serializers.ChoiceField(choices=MEALS)
    category = Food_Categories_SZ()

    class Meta:
        model = Food
        fields = '__all__'

    def validate_meals_fucus(self, value):
        if isinstance(value, int):
            return [value]
        return value

    def create(self, validated_data):
        try:
            validated_data["category"] = Food_Categories.objects.get(name=validated_data["category"]["name"])
        except Food_Categories.DoesNotExist:
            raise Food_Categories.DoesNotExist
        return super().create(validated_data)