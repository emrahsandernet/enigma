from django.shortcuts import render
from .models import UserKey, RegistryHelper

# Create your views here.

from rest_framework import generics
from .serializers import UserKeySerializer, RegistryHelperSerializer

class UserKeyList(generics.ListCreateAPIView):
    queryset = UserKey.objects.all()
    serializer_class = UserKeySerializer

class UserKeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserKey.objects.all()
    serializer_class = UserKeySerializer

class RegistryHelperList(generics.ListCreateAPIView):
    queryset = RegistryHelper.objects.all()
    serializer_class = RegistryHelperSerializer

class RegistryHelperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistryHelper.objects.all()
    serializer_class = RegistryHelperSerializer

    
