from rest_framework import serializers

from metabolic.models import Body_info, Metabolic

from meals.Utils.Diet_Calcuation import Metabolic_Calculator


class Body_info_SZ(serializers.ModelSerializer):
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
        instance, created = Body_info.objects.get_or_create(
            age = validated_data.get("age"),
            weight = validated_data.get("weight"),
            height = validated_data.get("height"),
            gender = validated_data.get("gender"),
            general_activities = validated_data.get("general_activities"),
            excise_activity = validated_data.get("excise_activity")
        )
        if created:
            cal = Metabolic_Calculator(instance)
            ret = Metabolic.objects.create(
                total_kcalorie = cal.total_kcalorie,
                total_protein = cal.total_protein,
                total_fat = cal.total_fat,
                total_carbohydrate = cal.total_carbohydrate,
                body_info = instance
            )
        else :
            instance.countUp()
            ret = Metabolic.objects.get(body_info_id=instance.id)
        return ret