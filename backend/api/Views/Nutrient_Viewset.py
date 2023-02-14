from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from api.Serialzier.Diet_Calcuation_SZ import Diet_Calcuation_SZ

from api.Utils.msg_utils import error_msg

class Nnutrient_Viewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = Diet_Calcuation_SZ

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(request, serializer.data)
            return Response(rtn, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)