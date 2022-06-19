
def client_identifications_middleware(get_response):

    def middleware(request):
        request.nonce = request.headers.get('nonce')
        request.port = request.headers.get('port')

        response = get_response(request)

        return response

    return middleware
