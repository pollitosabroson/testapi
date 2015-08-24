from django.conf.urls import url

from .views import users, userdetail

urlpatterns = [
    url(r'^users$', users),
    url(r'^users/(?P<pk>[0-9]+)/$', userdetail),
]
