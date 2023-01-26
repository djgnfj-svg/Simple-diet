from rest_framework import viewsets

from foods.models import Food_data

from api.Serialzier.Food_SZ import Food_SZ

class Food_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_SZ
    queryset = Food_data.objects.order_by("-id")
