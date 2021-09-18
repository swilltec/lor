import logging

from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from core import models
from . import serializers
from .utils import OneAPIUtility, FavoriteUtility


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

    def list(self, request: Request) -> Response:
        """Returns all characters in Lord of the Rings"""
        try:
           data = OneAPIUtility.fetch_all_characters()
           return Response(data)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False,
            url_path="(?P<character_id>[^/.]+)/quotes")
    def quotes(self, request: Request, character_id: str = None) -> Response:
        try:
           data = OneAPIUtility.fetch_all_character_quotes(character_id)
           return Response(data)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, url_path="(?P<character_id>[^/.]+)/favorites")
    def favorite_character(self, request: Response, character_id: str = None) -> Response:
        """View to favorite a specific character"""

        try:
            character = OneAPIUtility.fetch_character_or_quote(
                item_id=character_id, item_type='character')
            if character.get('total', 0) == 1:
                favourite = FavoriteUtility.create_character_favourite(
                    user=request.user,
                    details=character.get('docs')[0])
                serialized_favourite = serializers.FavoriteSerializer(
                    favourite)
                return Response(data=serialized_favourite.data, status=status.HTTP_201_CREATED)

            else:
                return Response(data={"message": "Item does not exist. please check favorite id"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False,
            url_path="(?P<character_id>[^/.]+)/quotes/(?P<quote_id>[^/.]+)/favorites")
    def favorite_quote(self, request: Response, character_id: str = None, quote_id: str = None) -> Response:
        """View to favorite a specific character quote"""

        try:
            character = OneAPIUtility.fetch_character_or_quote(
                item_id=quote_id, item_type='quote')
            if character.get('total', 0) == 1:
                favourite = FavoriteUtility.create_quote_favourite(
                    user=request.user,
                    details=character.get('docs')[0])
                serialized_favourite = serializers.FavoriteSerializer(
                    favourite)
                return Response(data=serialized_favourite.data, status=status.HTTP_201_CREATED)

            else:
                return Response(data={"message": "Item does not exist. please check favorite id"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            logger.error(e)
            return Response(data={"message": "Oops request failed. Try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class FavoriteViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for Favorites.
    """

    def list(self, request):
        queryset = models.Favorites.objects.filter(user=request.user)
        serializer = serializers.FavoriteSerializer(queryset, many=True)
        return Response(serializer.data)

