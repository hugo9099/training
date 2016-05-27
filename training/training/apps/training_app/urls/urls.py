from __future__ import unicode_literals

from django.conf.urls import patterns
from rest_framework import routers

from training.apps.training_app import views


router = routers.SimpleRouter(trailing_slash=True)
router.register(r'cities', views.CityViewSet)



urlpatterns = patterns('training.apps.training_app',)
urlpatterns += router.urls
