from rest_framework import routers

from api.Views.Nutrient_Viewset import Nnutrient_Viewset
from api.Views.Diet_Viewset import Diet_Viewset
from api.Views.Food_Viewset import Food_Viewset

router = routers.DefaultRouter()
# b
router.register(r'calk-nutrient-rate', Nnutrient_Viewset, basename="calk_nutrient") # admin이 음식을 추가할때
router.register(r'managing-diet', Diet_Viewset, basename="diet") # admin이 음식을 추가할때
router.register(r'food', Food_Viewset, basename="food") # admin이 음식을 추가할때