from http.server import *
import random as rd

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = '/src/img/sukasuka/{}.jpg'.format(rd.randint(1, 125))
        self.send_response(301)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', url)
        self.end_headers()
        self.wfile.write("Sukasuka random image".encode())
        return

if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, handler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()