import requests
from django.conf import settings


def external_api_get(name):
    response = (requests.get('http://omdbapi.com/?t={}&apikey={}'.format(name, settings.OMDBKEY))).json()
    return response
