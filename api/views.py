import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import User


def Users(request):
    queryset = User.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')

def UserDetail(request, pk=None):
    if request.method == 'GET':
        queryset =  get_object_or_404(User, pk=pk)
        data = serializers.serialize('json', [queryset])
        return HttpResponse(data, content_type='application/json')
