import logging

from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core import models
from . import serializers
from .utils import OneAPIService


logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    List, Create view and delete system user accounts
    """

    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]


class LorViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving characters.
    """

    def list(self, request):
        """Returns all characters in Lord of the Rings"""
        try:
           data = OneAPIService.fetch_all_characters()
           return Response(data)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False,
            url_path="(?P<id>[^/.]+)/quotes")
    def quotes(
            self,
            request,
            id=None):
        try:
           data = OneAPIService.fetch_all_character_quotes(id)
           return Response(data)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
