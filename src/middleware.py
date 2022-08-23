from werkzeug.wrappers import Request
from .datamodel import DataModel


class middleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        if "cja." in request.url:
            return self.app(environ, start_response)
        
        
        environ["cja.logger"] = data = DataModel()
        data.set_request(request)
        
        def __start_response(status, headers, *args):
            result = start_response(status, headers, *args)
            data.set_response(status, headers)
            return result
            
        return self.app(environ, __start_response)