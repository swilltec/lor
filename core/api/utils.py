import requests

from django.conf import settings


class OneAPIService:

    @staticmethod
    def _send_request(route):
        headers = {'Authorization': f'Bearer {settings.THE_ONE_API_KEY}'}
        url = "https://the-one-api.dev/v2/{}".format(route)
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def fetch_all_characters(cls):
        res = cls._send_request('character')
        return res

    @classmethod
    def fetch_all_character_quotes(cls, id: str):
        route = "character/{}/quote".format(id)
        res = cls._send_request(route)
        return res
