
from meals.Utils.Diet_Manager import Diet_Manager

from managers.models import Diet_nutrient_manager


def manager_update():
    Diet_nutrient_manager.objects.all().delete()
    simuldata = Diet_Manager()
