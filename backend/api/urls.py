from rest_framework import routers

from api.Views.Diet_Calcuation_Viewset import Diet_Calcuation_Viewset
from api.Views.Diet_Managing_Viewset import Diet_Managing_Viewset
from api.Views.Food_Viewset import Food_Viewset
from api.Views.Food_Categories_Viewset import Food_Categories_Viewset

router = routers.DefaultRouter()
# b
router.register(r'cal-diet', Diet_Calcuation_Viewset, basename="diet_cal") # admin이 음식을 추가할때
router.register(r'managing-diet', Diet_Managing_Viewset, basename="diet_managing") # admin이 음식을 추가할때
router.register(r'food', Food_Viewset, basename="food") # admin이 음식을 추가할때
router.register(r'food-category', Food_Categories_Viewset, basename="food-categories") # admin이 음식을 추가할때