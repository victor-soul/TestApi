from werkzeug.exceptions import Unauthorized

class Validator:

    def __init__(self, request):
        self.__request = request
    
    def validate(self):
        query = self.__request.args.get('query')
        if query is None:
            raise ValueError(('Unprocessable Entity query parameter is required',))

        headers = {k:v for k, v in self.__request.headers.items()}
        authorization = headers.get('Authorization')
        if authorization is None:
            raise Unauthorized(description='Missing Authorization header is required')