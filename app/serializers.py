#serializers.py 
#
import json
from rest_framework import serializers

from .models import UserKey, RegistryHelper

class UserKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserKey
        fields = "__all__"

class RegistryHelperSerializer(serializers.ModelSerializer):
    key_hive = serializers.CharField(max_length=255)

    class Meta:
        model = RegistryHelper
        fields = "__all__"

        