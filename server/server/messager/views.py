
from .models import Client
from . import messages
from .utils import ok_response, nok_response, send_message_to_client


def presence(request):
    try:
        client = Client.objects.get(port=request.port)
        client.save()
        return ok_response(request.nonce)
    except Client.DoesNotExist:
        return nok_response(request.nonce, messages.YOU_ARE_NOT_REGISTERED)


def register(request, username):
    if Client.objects.filter(username=username).exists():
        if Client.objects.get(username=username).port == request.port:
            return nok_response(request.nonce, messages.YOU_ARE_ALREADY_REGISTERED)
        return nok_response(request.nonce, messages.USERNAME_ALREADY_TAKEN)
    client = Client(username=username, port=request.port)
    client.save()
    return ok_response(request.nonce)


def unregister(request):
    try:
        client = Client.objects.get(port=request.port)
        client.delete()
        return ok_response(request.nonce)
    except Client.DoesNotExist:
        return nok_response(nonce=request.nonce, reason=messages.YOU_ARE_NOT_REGISTERED)


def send_message(request, username):
    message = request.GET.get('message')

    try:
        sender = Client.objects.get(port=request.port)
    except Client.DoesNotExist:
        return nok_response(request.nonce, messages.YOU_ARE_NOT_REGISTERED)

    # to become present
    sender.save()

    try:
        receiver = Client.objects.get(username=username)
    except Client.DoesNotExist:
        return nok_response(request.nonce, messages.USER_NOT_REGISTERED)

    if not receiver.is_present:
        return nok_response(request.nonce, messages.RECEIVER_IS_NOT_PRESENT)

    response = send_message_to_client(receiver.port,
                                      f"You have message from {sender.username}! message text:\n {message}")
    if response.status_code != 200:
        return nok_response(request.nonce, messages.ERROR_SENDING_MESSAGE)

    return ok_response(request.nonce)


