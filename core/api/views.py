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


class LorViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving characters.
    """

    def list(self, request: Request) -> Response:
        """Returns all characters in Lord of the Rings"""
        try:
            # Fetch all characters from endpoint
            data = OneAPIUtility.fetch_all_characters()
            return Response(data)
        except Exception as e:
            logger.error(e)
            # Returns a failed response fetch fails
            return Response(
                data={"message": "Oops request failed. Try again later"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, url_path="(?P<character_id>[^/.]+)/quotes")
    def quotes(self, request: Request, character_id: str = None) -> Response:
        try:
            # Fetch all characters quotes from endpoint
            data = OneAPIUtility.fetch_all_character_quotes(character_id)
            return Response(data)
        except Exception as e:
            logger.error(e)
            # Returns a failed response fetch fails if an error occurs during fetch request
            return Response(
                data={"message": "Oops request failed. Try again later"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, url_path="(?P<character_id>[^/.]+)/favorites")
    def favorite_character(
        self, request: Response, character_id: str = None
    ) -> Response:
        """View to favorite a specific character"""

        try:
            # Fetch character from api endpoint with character ID
            character = OneAPIUtility.fetch_character_or_quote(
                item_id=character_id, item_type="character"
            )

            # Checks the existence of a character and favorites if it exist
            if character.get("total", 0) == 1:
                favourite = FavoriteUtility.create_character_favourite(
                    user=request.user, details=character.get("docs")[0]
                )
                serialized_favourite = serializers.FavoriteSerializer(favourite)
                return Response(
                    data=serialized_favourite.data, status=status.HTTP_201_CREATED
                )

            else:
                # Returns item not found if character does not exist
                return Response(
                    data={"message": "Item does not exist. please check favorite id"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        except Exception as e:
            logger.error(e)
            # Returns a failed response fetch fails if an error occurs during fetch request
            return Response(
                data={"message": "Oops request failed. Try again later"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(
        detail=False,
        url_path="(?P<character_id>[^/.]+)/quotes/(?P<quote_id>[^/.]+)/favorites",
    )
    def favorite_quote(
        self, request: Response, character_id: str = None, quote_id: str = None
    ) -> Response:
        """View to favorite a specific character quote"""

        try:
            # Fetch character quote from api endpoint with quote ID
            character = OneAPIUtility.fetch_character_or_quote(
                item_id=quote_id, item_type="quote"
            )

            # Checks the existence of a character and favorites if it exist
            if character.get("total", 0) == 1:
                favourite = FavoriteUtility.create_quote_favourite(
                    user=request.user, details=character.get("docs")[0]
                )
                serialized_favourite = serializers.FavoriteSerializer(favourite)
                return Response(
                    data=serialized_favourite.data, status=status.HTTP_201_CREATED
                )

            else:
                # Returns item not found if quote does not exist
                return Response(
                    data={"message": "Item does not exist. please check favorite id"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        except Exception as e:
            logger.error(e)
            # Returns a failed response fetch fails if an error occurs during fetch request
            return Response(
                data={"message": "Oops request failed. Try again later"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class FavoriteViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for Favorites.
    """

    def list(self, request):
        """Returns all authenticated user’s favorited items"""
        queryset = models.Favorites.objects.filter(user=request.user)
        serializer = serializers.FavoriteSerializer(queryset, many=True)
        return Response(serializer.data)
