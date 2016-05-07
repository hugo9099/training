from django.shortcuts import render
from rest_framework import filters, viewsets

# Create your views here.
from .serializers import CitySerializer
from .models import City
from rest_framework import filters
from rest_framework.decorators import permission_classes
from permission_classes import *


class CityViewSet(viewsets.ModelViewSet):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, filters.DjangoFilterBackend)
    search_fields = ('zip_code', 'city')
    ordering_fields = ('zip_code', 'city')
    filter_fields = ('state',)

    def list(self, request, *args, **kwargs):
        """
        state -- state (US state)
        """
        return super(CityViewSet, self).list(request, *args, **kwargs)


@permission_classes((WhiteListorAPIPermission,))
class LeadViewSet(viewsets.ModelViewSet):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()