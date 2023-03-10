from rest_framework import routers

from api.Views.Metabolic_Viewset import Metabolic_Viewset
from api.Views.Diet_Viewset import Diet_Viewset
from api.Views.Food_Viewset import Food_Viewset
from api.Views.Food_Categories_Viewset import Food_Categories_Viewset

router = routers.DefaultRouter()

router.register(r'diet', Diet_Viewset, basename="diet")
router.register(r'foods', Food_Viewset, basename="foods")
router.register(r'metabolic', Metabolic_Viewset, basename="metabolic")
router.register(r'food-categories', Food_Categories_Viewset, basename="food-categories")