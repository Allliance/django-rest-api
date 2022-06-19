from django.http import HttpResponse
import requests


def send_message_to_client(port, message):
    url = f"http://127.0.0.1:{port}/receive/"
    return requests.post(url, data={"message": message})


def ok_response(nonce):
    return HttpResponse(f"ok {nonce}")


def nok_response(nonce, reason):
    return HttpResponse(f"nok {reason} {nonce}")