from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from foods.models import Food_data

from django.db import IntegrityError
from api.Serialzier.Food_SZ import Food_SZ

from api.Utils.msg_utils import error_msg

class Food_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_SZ
    queryset = Food_data.objects.order_by("-id")
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                rtn = serializer.create(serializer.data)
            except IntegrityError:
                return Response(error_msg(4041), status=status.HTTP_400_BAD_REQUEST)
            return Response(rtn, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)