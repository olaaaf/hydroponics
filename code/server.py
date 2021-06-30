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
        self._set_response()
        file = None
        if self.path == '/' or self.path == '/index.html':   
            file = open('website/index.html', 'rb')
        else:
            if os.path.isfile('website/' +self.path):
                file = open('website/' + self.path, 'rb')
            else:
                #Handle 404 Request
                file = open('website/404.html', 'rb') 
        self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        data_json = json.loads(post_data.decode('utf8').replace("'", '"'))
        with open('test.json', 'w', encoding='utf-8') as file:
            json.dump(data_json, file)
        self._set_response('application/json')
        self.wfile.write(json.dumps(data_json).encode('utf-8')) 

def start_server(port=80):
    server_adress = ('', port)
    os.chdir(pathlib.Path(__file__).parent.resolve())
    server = HTTPServer(server_address=server_adress, RequestHandlerClass=Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    logging.info('Stopping http server...\n')

if __name__=="__main__":
    start_server()