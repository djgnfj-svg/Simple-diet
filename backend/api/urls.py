from rest_framework import routers

from api.Views.Metabolic_Calc_Viewset import Metabolic_Calc_Viewset
from api.Views.Diet_Managing_Viewset import Diet_Managing_Viewset
from api.Views.Food_Viewset import Food_Viewset
from api.Views.Food_Categories_Viewset import Food_Categories_Viewset

router = routers.DefaultRouter()
router.register(r'calc-metabolic', Metabolic_Calc_Viewset, basename="metabolic-cal")
router.register(r'managing-diet', Diet_Managing_Viewset, basename="diet-managing")
router.register(r'food', Food_Viewset, basename="food")
router.register(r'food-category', Food_Categories_Viewset, basename="food-categories")