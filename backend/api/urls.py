from rest_framework import routers

from api.Views.Metabolic_rate_ViewSet import Metabolic_rate_ViewSet
from api.Views.Diet_Managing_Viewset import Diet_Managing_Viewset
from api.Views.Food_Viewset import Food_Viewset

router = routers.DefaultRouter()
router.register(r'calk_metabolic_rate', Metabolic_rate_ViewSet, basename="calk_metabolic") # admin이 음식을 추가할때
router.register(r'diet_diet', Diet_Managing_Viewset, basename="diet") # admin이 음식을 추가할때
router.register(r'food', Food_Viewset, basename="food") # admin이 음식을 추가할때