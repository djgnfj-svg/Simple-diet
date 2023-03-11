from rest_framework import serializers

from foods.models import Food_Categories


class Food_Categories_SZ(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Food_Categories
        fields = ['name']