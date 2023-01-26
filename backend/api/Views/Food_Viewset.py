from rest_framework import status, viewsets
from rest_framework.response import Response

from api.Utils.msg_utils import error_msg
from api.Serialzier.Food_SZ import Food_SZ
from foods.models import Food_data

class Food_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_SZ
    queryset = Food_data.objects.order_by("-id")
