from flask import request, render_template

class HttpHandler():
    
    def __init__(self) -> None:
        pass

    def get_viewer():
        return render_template("index.html")