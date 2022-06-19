from . import models
import requests
from django.conf import settings


def request_server(request, url):
    complete_url = settings.SERVER_ADDRESS + url
    command = models.Command()
    command.save()
    return requests.get(complete_url, headers={'nonce': str(command.pk),
                                               'port': str(request.META['SERVER_PORT'])})
