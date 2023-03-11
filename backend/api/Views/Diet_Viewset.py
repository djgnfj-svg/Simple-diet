from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from api.Utils.msg_utils import error_msg

from api.Serialzier.Diet_SZ import Diet_SZ

class Diet_Viewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = Diet_SZ
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(serializer.data)
            return Response(rtn, status=status.HTTP_201_CREATED)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)