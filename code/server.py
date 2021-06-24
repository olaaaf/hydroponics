from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os
import json

web_dir = os.path.join(os.path.dirname(__file__), 'website')
server_adress = ('', 8000)

class Handler(BaseHTTPRequestHandler):
    
    def _set_response(self, type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def do_GET(self):
        self._set_response()
        file = open('website/index.html', 'rb')
        self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        data_json = json.loads(post_data.decode('utf8').replace("'", '"'))
        data_json["param1"] += 100
        self._set_response('application/json')
        self.wfile.write(json.dumps(data_json).encode('utf-8')) 

def main():
    server = HTTPServer(server_address=server_adress, RequestHandlerClass=Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    logging.info('Stopping http server...\n')

if __name__=="__main__":
    main()