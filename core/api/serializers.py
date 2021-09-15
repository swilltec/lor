from rest_framework import serializers
from core import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
