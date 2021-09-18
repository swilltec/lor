import requests
from typing import Dict, Any

from django.conf import settings
from core import models


class OneAPIUtility:
    """The One Api Service

    It contains the various utility methods to query
    the one-api endpoint
    """

    @staticmethod
    def _send_request(route):
        headers = {"Authorization": f"Bearer {settings.THE_ONE_API_KEY}"}
        url = "https://the-one-api.dev/v2/{}".format(route)
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def fetch_all_characters(cls) -> Dict[str, Any]:
        """Fetch all characters in LotR movie/book"""
        res = cls._send_request("character")
        return res

    @classmethod
    def fetch_all_character_quotes(cls, character_id: str) -> Dict[str, Any]:
        """Fetch all character quotes in LotR movie/book"""
        route = "character/{}/quote".format(character_id)
        res = cls._send_request(route)
        return res

    @classmethod
    def fetch_character_or_quote(cls, item_type: str, item_id: str) -> Dict[str, Any]:
        """Fetch character/quote by id"""
        route = "{}/{}".format(item_type, item_id)
        res = cls._send_request(route)
        return res


class FavoriteUtility:
    """Favorite utility class"""

    @staticmethod
    def _create_character(details: dict) -> models.Character:
        """Create a new character"""
        character = models.Character.objects.create(
            item_id=details.get("_id"),
            height=details.get("height"),
            race=details.get("race"),
            gender=details.get("gender"),
            birth=details.get("birth"),
            spouse=details.get("spouse"),
            death=details.get("death"),
            realm=details.get("realm"),
            heir=details.get("heir"),
            name=details.get("name"),
            wiki_url=details.get("wiki_url"),
        )
        return character

    @classmethod
    def _create_quote(cls, details: dict) -> models.Quote:
        """Create a new quote"""
        # fetch details of the author of the quote
        character_details = OneAPIUtility.fetch_character_or_quote(
            item_id=details.get("character"), item_type="character"
        ).get("docs")[0]

        # Create an object of the author
        character = cls._create_character(character_details)

        quote = models.Quote.objects.create(
            item_id=details.get("_id"),
            movie=details.get("movie"),
            dialog=details.get("race"),
            character=character,
        )
        return quote

    @classmethod
    def create_character_favourite(
        cls, user: models.CustomUser, details: dict
    ) -> models.Favorites:
        """Create favourite character"""
        # Create character instance
        character = cls._create_character(details)

        fav = models.Favorites.objects.create(
            user=user,
            character=character,
        )
        return fav

    @classmethod
    def create_quote_favourite(
        cls,
        user: models.CustomUser,
        details: dict,
    ) -> models.Favorites:
        """Create favourite quote"""
        # Create quote instance
        quote = cls._create_quote(details)

        fav = models.Favorites.objects.create(
            user=user,
            quote=quote,
        )
        return fav
