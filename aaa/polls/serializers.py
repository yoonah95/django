from rest_framework import serializers
from .models import *
class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ('iid','ppw',)