from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from api.Utils.msg_utils import error_msg

from api.Serialzier.User_Metabolic import User_body_info_SZ

class Diet_Managing_Viewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = User_body_info_SZ

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(request, serializer.data)
            return Response(rtn, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)