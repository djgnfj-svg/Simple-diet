from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from api.Serialzier.Metabolic_SZ import Body_info_SZ, Metabolic_Output_SZ

from api.Utils.msg_utils import error_msg

class Metabolic_Viewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = Body_info_SZ
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ret = serializer.create(serializer.data)
            return Response(Metabolic_Output_SZ(ret).data, status=status.HTTP_200_OK)
        return Response(error_msg(serializer=serializer), status=status.HTTP_400_BAD_REQUEST)