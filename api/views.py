from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import User


def users(request):
    if request.method == 'POST':
        user_save = serializers.deserialize("json", request.POST['data'])
        for deserialized_object in user_save:
            deserialized_object.save()
            return HttpResponse(request.DATA, content_type='application/json')
    elif request.method == 'GET':
        queryset = User.objects.all()
        data = serializers.serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')


def userdetail(request, pk=None):
    if request.method == 'GET':
        queryset = get_object_or_404(User, pk=pk)
        data = serializers.serialize('json', [queryset])
        return HttpResponse(data, content_type='application/json')
