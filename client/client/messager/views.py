from . import server_api
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def presence(request):
    return HttpResponse(server_api.request_server(request, "/presence"))


def register(request, username):
    return HttpResponse(server_api.request_server(request, f"/register/{username}"))


def unregister(request):
    return HttpResponse(server_api.request_server(request, f"/unregister"))


def send_message(request, username):
    message = request.GET.get('message')

    return HttpResponse(server_api.request_server(request, f"/send_message/{username}?message={message}"))


@csrf_exempt
def receive_message(request):
    print("new response received! :")
    print(request.POST.get("message"))
    return HttpResponse("received")


