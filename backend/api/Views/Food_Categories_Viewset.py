from rest_framework import status, viewsets, mixins

from foods.models import Food_Categories

from api.Serialzier.Food_Categories_SZ import Food_Categories_SZ


class Food_Categories_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_Categories_SZ
    queryset = Food_Categories.objects.order_by("-id")