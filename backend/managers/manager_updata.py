
from managers.models import Diet_nutrient_manager


def manager_update():
    Diet_nutrient_manager.objects.all().delete()
    