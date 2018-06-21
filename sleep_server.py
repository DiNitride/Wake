from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class WakeServer(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content:type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf:8'))
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


server = HTTPServer(("0.0.0.0", 9895), WakeServer)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
