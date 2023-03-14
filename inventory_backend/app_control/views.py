from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Inventory, InventorySerializer, InventoryGroup, InventoryGroupSerializer
)
from rest_framework.response import Response
from api.custom_method import IsAuthenticatedCustom



class InventoryView(ModelViewSet):
    queryset = InventoryGroup.objects.select_related('belongs_to','created_by').prefetch_related('inventories')
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticatedCustom, )

    def create(self, request, *args, **kwargs):
        request.data.update({'created_by_id':request.user.id})
        return super().create(request, *args, **kwargs)
