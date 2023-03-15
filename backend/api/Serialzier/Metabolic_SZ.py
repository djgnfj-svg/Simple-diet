from rest_framework import serializers

class Metabolic_SZ(serializers.Serializer):
    total_kcalorie = serializers.ReadOnlyField()
    total_protein = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_carbohydrate = serializers.ReadOnlyField()