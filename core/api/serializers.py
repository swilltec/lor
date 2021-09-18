from typing import Dict
from rest_framework import serializers
from core import models
from .utils import OneAPIUtility


class FavoriteSerializer(serializers.ModelSerializer):
    """A Favorite ModelSerializer controls which fields should be displayed."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Favorites
        fields = "__all__"
        depth = 2  # Display details of relational models
