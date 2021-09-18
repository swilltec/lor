from typing import Dict
from rest_framework import serializers
from core import models
from .utils import OneAPIUtility


class UserSerializer(serializers.ModelSerializer):
    """A User ModelSerializer controls which fields should be displayed."""
    class Meta:
        model = models.CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class FavoriteSerializer(serializers.ModelSerializer):
    """A Favorite ModelSerializer controls which fields should be displayed."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Favorites
        fields = '__all__'
        depth = 2
