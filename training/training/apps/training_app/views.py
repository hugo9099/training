from django.shortcuts import render

# Create your views here.
from .serializers import CitySerializer
from .models import City
from rest_framework import filters,status, viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from permission_classes import *
from classbuilder import *
import viewbuilder
import json


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

@permission_classes((WhiteListorAPIPermission,))
@api_view(['GET'])
def FieldType(request):
    b_c = builderClass()
    # data = {'data_type': TYPE_Choice,
    #         'data_field': b_c.field,
    #         'data_admin': b_c.admin,
    #         'data_serializer': b_c.serializer,
    #         'data_class': b_c.map_class
    #         }
    return Response({}, status=status.HTTP_200_OK)


@api_view(['GET'])
def build_class(request):
    try:
        data = request.query_params
        name = request.GET.get('name')
        field_list = request.GET.getlist('fields')
        dict_list= []
        for element in field_list:
            dict_list.append(json.loads(element))
        b_c = builderClass(data['name'], dict_list)
        class_str = b_c.generate_class()
        admin_str = b_c.generate_admin()
        serializer_str = b_c.generate_serializer()
        viewset_str = b_c.generate_viewset()
        url_str = b_c.generate_url()
        data = {'class_str':class_str,
                'admin_str':admin_str,
                'serializer_str': serializer_str,
                'viewset_str':viewset_str,
                'url_str':url_str
                }

        # html_add = viewbuilder.generate_html_add(dict_list, name)
        # html_page = viewbuilder.generate_html_page(dict_list, name)
        # javascritp_add = viewbuilder.generate_javascritp_add(dict_list, name)
        # javascritp_html_page = viewbuilder.generate_javascritp_html_page(dict_list, name)
        #
        #
        # data = {'class_str':html_add,
        #         'admin_str':html_page,
        #         'serializer_str': javascritp_add,
        #         'viewset_str':javascritp_html_page
        #         }




        status_http = status.HTTP_200_OK
    except Exception, e:
        data = {'error': e.message}
        status_http = status.HTTP_403_FORBIDDEN

    return Response(data=data, status=status_http)

@api_view(['GET'])
def build_view(request):
    try:
        data = request.query_params
        name = request.GET.get('name')
        field_list = request.GET.getlist('fields')
        dict_list= []
        for element in field_list:
            dict_list.append(json.loads(element))

        html_add = viewbuilder.generate_html_add(dict_list, name)
        html_page = viewbuilder.generate_html_page(dict_list, name)
        javascritp_add = viewbuilder.generate_javascritp_add(dict_list, name)
        javascritp_html_page = viewbuilder.generate_javascritp_html_page(dict_list, name)

        data = {'html_add':html_add,
                'html_page':html_page,
                'javascritp_add': javascritp_add,
                'javascritp_html_page':javascritp_html_page
                }
        status_http = status.HTTP_200_OK
    except Exception, e:
        data = {'error': e.message}
        status_http = status.HTTP_403_FORBIDDEN

    return Response(data=data, status=status_http)


