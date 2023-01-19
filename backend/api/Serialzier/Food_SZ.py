from rest_framework import serializers

from foods.models import Food_data



class Food_SZ(serializers.ModelSerializer):
    fucus = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    kcalorie = serializers.IntegerField(default=0)
    carbohydrate = serializers.IntegerField(default=0)
    protein = serializers.IntegerField(default=0)
    fat = serializers.IntegerField(default=0)
    price = serializers.IntegerField()
    food_number = serializers.IntegerField()
    food_gram = serializers.IntegerField()
    link = serializers.URLField(max_length=200)

    
    class Meta:
        model = Food_data
        fields = "__all__"