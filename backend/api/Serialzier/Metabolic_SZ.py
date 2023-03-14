from rest_framework import serializers

from metabolic.models import Metabolic



class Metabolic_SZ(serializers.ModelSerializer):
    total_kcalorie = serializers.ReadOnlyField()
    total_protein = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_carbohydrate = serializers.ReadOnlyField()

    class Meta:
        model = Metabolic
        fields = ("total_kcalorie", "total_protein", "total_fat", "total_carbohydrate")