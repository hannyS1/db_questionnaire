from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AccessControlMiddleware(MiddlewareMixin):

    def process_response(self, request, response: HttpResponse):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
