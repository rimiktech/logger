import uuid
import json
from datetime import datetime
from .queue import queue

class DataModel:
    request_id = None
    client_ip = None
    request_time = None
    request_url = None
    request_method = None
    request_headers = None
    request_payload = None
    response_status = None
    response_headers = None
    taken_time = None
    last_updated = None
    messages = []

    def __init__(self, **args) -> None:
        self.request_id = uuid.uuid4()
        self.request_time = datetime.utcnow()

    
    def set_request(self, request):
        self.client_ip = request.remote_addr
        self.request_url = request.url
        #self.request_headers = request.headers
        self.request_method = request.method
        self.request_payload = self.__get_posted_data(request)
        queue.put(self)

    
    def set_response(self, status, headers, response = None):
        self.taken_time = 1000.0 * (datetime.utcnow() - self.request_time).total_seconds()
        self.response_status = status
        self.response_headers = headers
        queue.put(self)
    
    
    def set_message(self, message):
        self.messages.append({ "message": message, "time": datetime.utcnow() })
        queue.put(self)
    
    
    
    def __get_posted_data(self, request):
        cnt = request.content_type
        if cnt is None:
            return { }
        elif (cnt.startswith('application/json')):
            return json.loads(request.get_data().decode("utf-8"))
        elif(cnt.startswith("application/x-www-form-urlencoded") or cnt.startswith("multipart/form-data")):
            data = { }
            for key, value in request.form.items():
                if key.endswith('[]'):
                    data[key[:-2]] = request.form.getlist(key)
                else:
                    data[key] = value
            return data
    