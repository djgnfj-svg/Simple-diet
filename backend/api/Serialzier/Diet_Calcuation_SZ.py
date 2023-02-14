from rest_framework import serializers

from diet_meals.Utils.Diet_Calcuation import Diet_Calculator

class Diet_Calcuation_SZ(serializers.Serializer):
    age = serializers.IntegerField(min_value=20, max_value=100)
    weight = serializers.FloatField(min_value=40, max_value=250)
    height = serializers.FloatField(min_value=140, max_value=250)

    gender = serializers.CharField(max_length=2)
    general_activities = serializers.FloatField(min_value=1.2, max_value=1.6)
    excise_activity = serializers.FloatField(min_value=0, max_value=0.3)

    diet_status = serializers.FloatField(min_value=0.8, max_value=1.0)
    many_meals = serializers.IntegerField(min_value=2, max_value=3)
    
    def create(self, request, validated_data):
        instance = {}
        # todo 단백질계수와 지방 기본계수에대한 입력을 받자
        cal = Diet_Calculator(1.6, 0.28)
        cal.set_total_data(validated_data)
        instance["total_data"] = {}
        instance["total_data"] = cal.get_total_json_data()
        cal.Calk_diet(instance, validated_data["many_meals"], validated_data["diet_status"])

        return instance