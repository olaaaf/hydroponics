from settings import Settings
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import json
import pathlib

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
        port = settings.get_port()
        settings.load_new(data_json)
        if port != settings.get_port():
            restart_server()
        #Response to the client
        self._set_response('application/json')
        self.wfile.write(json.dumps(data_json).encode('utf-8'))

server = None
start = True
settings = {}

def stop_server():
    global server
    server.server_close()

def restart_server():
    global start
    start = True
    stop_server()

def start_server(set:Settings):
    global settings
    global server
    global start
    
    settings = set
    start = True
    os.chdir(pathlib.Path(__file__).parent.resolve())
    #Loop the server with restarting 
    while start and settings.get_start_server():
        start = False
        server_adress = ('', settings.get_port())
        server = HTTPServer(server_address=server_adress, RequestHandlerClass=Handler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        except OSError:
            logging.info ("Stopped the server.")
            if start:
                logging.info ("Restarting with new settings.")
    server.server_close()

if __name__=="__main__":
    start_server()