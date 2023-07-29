from django.shortcuts import render
from rest_framework import viewsets
from exelgen.models import XLModel
from .serializer import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = XLModel.objects.all()
    serializer_class = DataSerializer

    def perform_create(self, serializer):
        data = self.request.data
        name = data.get('data').get('data1').get('Имя')
        serializer.save(name=name)
    
    def perform_update(self, serializer):
        data = self.request.data
        name = data.get('data').get('data1').get('Имя')
        serializer.save(name=name)
