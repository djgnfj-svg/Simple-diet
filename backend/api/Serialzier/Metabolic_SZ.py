from rest_framework import serializers

from metabolic_calculator.models import Body_info

from meals.Utils.Diet_Calcuation import Metabolic_Calculator


class Metabolic_SZ(serializers.ModelSerializer):
    class Meta:
        model = Body_info
        exclude = ("id", "count", "created_at", "updated_at")

    GENDER_CHOICES = (
        ('M', 'M'),
        ('W', 'W'),
    )
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=40, max_value=150)
    height = serializers.FloatField(min_value=140, max_value=250)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)
    
    def create(self, validated_data):
        _age = validated_data.get("age")
        _weight = validated_data.get("weight")
        _height = validated_data.get("height")
        _gender = validated_data.get("gender")
        _general_activities = validated_data.get("general_activities")
        _excise_activity = validated_data.get("excise_activity")

        instance = Body_info(
            age = _age,
            weight = _weight,
            height = _height,
            gender = _gender,
            general_activities = _general_activities,
            excise_activity = _excise_activity
        )
        ret = {}
        cal = Metabolic_Calculator(instance)
        ret["total_kcalorie"] = cal.total_kcalorie
        ret["total_protein"] = cal.total_protein
        ret["total_fat"] = cal.total_fat
        ret["total_carbohydrate"] = cal.total_carbohydrate
        return ret