from django.conf.urls import url

from .views import Users, UserDetail

urlpatterns = [
    url(r'^users$', Users),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail),
]