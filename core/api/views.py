from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from core import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    List, Create view and delete system user accounts
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]
