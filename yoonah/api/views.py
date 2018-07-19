from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from rest_framework import filters

from rest_framework import viewsets

from rest_framework.decorators import detail_route

from rest_framework.response import Response
from django.http import HttpResponse

from .models import *
from .serializers import *




class SignViewSet(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer

def testview(request) :
	if request.method == 'post':
		print(request.post['clientid'])


