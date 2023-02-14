from rest_framework import serializers

from foods.models import Food_Categories

class Food_Categories_SZ(serializers.ModelSerializer):
    class Meta:
        model = Food_Categories
        fields = ['name']