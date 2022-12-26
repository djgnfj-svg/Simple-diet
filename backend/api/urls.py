from rest_framework import routers

from api.Views.Metabolic_rate_ViewSet import Metabolic_rate_ViewSet

router = routers.DefaultRouter()
router.register(r'calk_metabolic_rate', Metabolic_rate_ViewSet, basename="diet") # admin이 음식을 추가할때