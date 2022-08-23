from .httphandler import HttpHandler
from .middleware import middleware
from flask import request

class logger:
    
    @staticmethod
    def register(app):
        app.wsgi_app = middleware(app.wsgi_app)
        app.add_url_rule("/cja.logger", view_func=HttpHandler.get_viewer)

    @staticmethod
    def log(message):
        if "cja.logger" in request.environ and request.environ["cja.logger"]: 
            request.environ["cja.logger"].set_message(message)
        pass