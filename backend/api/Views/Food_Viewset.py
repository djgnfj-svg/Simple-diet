from rest_framework import status, viewsets
from rest_framework.response import Response

from api.Utils.msg_utils import error_msg
from api.Serialzier.Food_SZ import Food_SZ
from foods.models import Food_data

class Food_Viewset(viewsets.ModelViewSet):
    serializer_class = Food_SZ
    queryset = Food_data.objects.order_by("-id")[:10]
    def list(self, request, *args, **kwargs):
        if request.query_params:
            fucus = request.query_params.get("fucus",None)
            #페이지 네이션해줘야될듯하다
            self.queryset = Food_data.objects.filter(fucus=fucus).order_by("-id")[:10]
        return super().list(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)