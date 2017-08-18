from __future__ import unicode_literals

from django.conf.urls import patterns, url
from rest_framework import routers

from training.apps.training_app import views

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'cities', views.CityViewSet)

urlpatterns = patterns('training.apps.training_app',
                       url(r'^FieldType/$', views.FieldType, name='FieldType'),
                       url(r'^build-class/$', views.build_class, name='build-class'),
                       url(r'^build-view/$', views.build_view, name='build-view'),)

urlpatterns += router.urls
