from http.server import BaseHTTPRequestHandler, HTTPServer
import wakeonlan


class WakeServer(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content:type', 'text/html')
        self.end_headers()

    def do_GET(self):
        wakeonlan.send_magic_packet("D0:50:99:81:D5:A4", ip_address="192.168.1.7")
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf:8'))


server = HTTPServer(("0.0.0.0", 6578), WakeServer)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
