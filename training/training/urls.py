"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from training.libs.utils.static import staticfiles_urlpatterns as training_static

# bower_components_folder = os.path.abspath(os.path.join(settings.BASE_DIR, 'angular', 'src', 'crm', 'bower_components'))
app_dev_folder = os.path.abspath(os.path.join(settings.BASE_DIR, 'angular', 'src', 'crm', 'app'))
bower_components_folder = os.path.abspath(
    os.path.join(settings.BASE_DIR, 'angular', 'src', 'crm', 'bower_components'))

api_root = 'crm/api/v1/' if settings.DEBUG else 'api/v1/'
html_root = 'crm/' if settings.DEBUG else ''


def api(path):
    return r'^{}{}'.format(api_root, path)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(api('training/'), include('training.apps.training_app.urls.urls', namespace='training_app')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    # don't switch the order of the following lines because it will not work
    urlpatterns += training_static('crm/app', app_dev_folder, disable_caching=True)
    urlpatterns += training_static('crm/bower_components', bower_components_folder,
                                   disable_caching=False)
