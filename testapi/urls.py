from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^.*', views.AngularAppView.as_view(), name='app')
)
