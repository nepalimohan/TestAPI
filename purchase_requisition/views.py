from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializers
# Create your views here.


# class PurchaseRequisitionViewsets(viewsets.ViewSet):
#     def list(self, request):
#         query = models.PurchaseRequisition.objects.all()
#         serializer = serializers.PurchaseRequisition(query, many=True)
#         return Response(serializer.data)


class PurchaseRequisitionViewsets(viewsets.ModelViewSet):
    queryset = models.PurchaseRequisition.objects.all()
    serializer_class = serializers.PurchaseRequisition
    

class PurchaseRequisitionItemViewsets(viewsets.ModelViewSet):
    queryset = models.PurchaseRequisitionItem.objects.all()
    serializer_class = serializers.PurchaseItemListViewset
    