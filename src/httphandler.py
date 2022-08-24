from flask import request, render_template
import jinja2

class HttpHandler():

    TEMPLATE_PATH = "./src/templates"
    
    def __init__(self) -> None:
        pass

    def __render(template, **context):
        environ = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=HttpHandler.TEMPLATE_PATH))
        template = environ.get_template(template).render(context)
        return template
    
    def get_viewer():
        return HttpHandler.__render("index.html")