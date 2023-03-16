from rest_framework import serializers

from foods.models import Food, Food_Categories

from api.Serialzier.Food_Categories_SZ import Food_Categories_SZ

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
    
    category = Food_Categories_SZ()

    class Meta:
        model = Food
        fields = '__all__'

    def create(self, validated_data):
        try:
            validated_data["category"] = Food_Categories.objects.get(name=validated_data["category"]["name"])
        except Food_Categories.DoesNotExist:
            raise Food_Categories.DoesNotExist
        return super().create(validated_data)