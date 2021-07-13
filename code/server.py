from settings import Settings
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import json
import pathlib
import threading

class Handler(BaseHTTPRequestHandler):
    
    def _set_response(self, type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def do_GET(self):
        if ".css" in self.path:
            self._set_response('text/css')
        elif ".js" in self.path:
            self._set_response('text/javascript')
        elif ".json" in self.path:
            self._set_response('application/json')
        else:
            self._set_response()
        file = None
        if self.path == '/' or self.path == '/index.html':   
            file = open('website/index.html', 'rb')
        else:
            self.path = self.path[1:]
            if os.path.isfile(self.path):
                file = open(self.path, 'rb')
            else:
                #Handle 404 Request
                file = open('website/404.html', 'rb') 
        self.wfile.write(file.read())

    def do_POST(self):
        #Get POST data size
        content_length = int(self.headers['Content-Length'])
        #Get POST data
        post_data = self.rfile.read(content_length)
        #Convert data to json
        data_json = json.loads(post_data.decode('utf8').replace("'", '"'))
        #Handle new settings
        global settings
        settings.load_new(data_json)
        #Response to the client
        self._set_response('application/json')
        self.wfile.write(json.dumps(data_json).encode('utf-8'))

server = None
running = False
settings = {}
thread = None

def start(port=80):
    global thread, server, running
    running = True
    #Server addres with the port from settings
    server_adress = ('', port)
    #Set up the server with the custom handler class
    server = HTTPServer(server_address=server_adress, RequestHandlerClass=Handler)
    #Server will run on a sepparate thread - allowing us to kill it
    thread = threading.Thread(target=server.serve_forever)
    #Start the server
    thread.start()

def start_server(set:Settings):
    global settings, server, start
    settings = set
    #Set the current working directory to wherever the code is located
    os.chdir(pathlib.Path(__file__).parent.resolve())
    if settings.get_start_server():
        start(settings.get_port())

if __name__=="__main__":
    start()