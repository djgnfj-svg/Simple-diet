from rest_framework import serializers
from metabolic_calculator.models import Body_info

from meals.Utils.Diet_Calcuation import Metabolic_Calculator

class Body_info_SZ(serializers.ModelSerializer):
    class Meta:
        model = Body_info
        exclude = ("id", "count", "created_at", "updated_at")
    
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=40, max_value=150)
    height = serializers.FloatField(min_value=140, max_value=250)
    gender = serializers.ChoiceField(GENDER_CHOICES)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)
    
    def create(self, validated_data):
        try :
            instnace = Body_info.objects.get(
                age = validated_data["age"],
                weight = validated_data["weight"],
                height = validated_data["height"],
                gender = validated_data["gender"],
                general_activities = validated_data["general_activities"],
                excise_activity = validated_data["excise_activity"],
            )
        except Body_info.DoesNotExist as e:
            instnace = Body_info.objects.create(
                age = validated_data["age"],
                weight = validated_data["weight"],
                height = validated_data["height"],
                gender = validated_data["gender"],
                general_activities = validated_data["general_activities"],
                excise_activity = validated_data["excise_activity"],
            )
        else:
            instnace.count += 1
        instnace.save()
        return instnace
    

class Metabolic_Output_SZ(serializers.Serializer):
    # todo 이렇게 만든 데이터를 세이브...?
    def to_representation(self, instance):
        ret = {}
        cal = Metabolic_Calculator(instance, 1.6, 0.28)
        ret["total_kcalorie"] = cal.total_kcalorie
        ret["total_protein"] = cal.total_protein
        ret["total_fat"] = cal.total_fat
        ret["total_carbohydrate"] = cal.total_carbohydrate
        return ret