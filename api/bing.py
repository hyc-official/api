from http.server import *
import requests as rq
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        rp = rq.get(url='https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        dt = rp.json()
        url = 'https://cn.bing.com' + dt['images'][0]['url']
        self.send_response(302)
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'max-age=300')
        self.send_header('Location', url)
        self.end_headers()
        self.wfile.write("Bing image".encode())
        return

if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, handler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()