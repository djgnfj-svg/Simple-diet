from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from foods.models import Food_Categories, Food

from django.db import IntegrityError
from django.db.models import Q

from api.Serialzier.Food_SZ import Food_SZ

from api.Utils.msg_utils import error_msg

class Food_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_SZ
    queryset = Food.objects.order_by("-id")
    
    # 음식을 쿼리로 받아서 정렬해서 보낸다
    # 탄단지를 선택해서 정렬을 선택 할 수 있다.
    def list(self, request, *args, **kwargs):
        if request.query_params:
            name = request.query_params.get("name", None)
            sort_nutrient = request.query_params.get("sort_nutrient", None)
            q = Q()

            if name :
                q &= Q(name__icontains=name)
                
            rtn = Food.objects.filter(q)    
            if sort_nutrient:
                rtn = rtn.order_by(sort_nutrient)
            return Response(self.get_serializer(rtn, many=True).data, status=status.HTTP_200_OK)
        
        return super().list(request, *args, **kwargs)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.create(serializer.data)
            except IntegrityError:
                return Response(error_msg(4041), status=status.HTTP_400_BAD_REQUEST)
            except Food_Categories.DoesNotExist:
                return Response(error_msg(4042), status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)