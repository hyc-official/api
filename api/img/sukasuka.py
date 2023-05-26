from http.server import *
import random as rd
import requests as rq

head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = 'https://raw.githubusercontent.com/hyc1230/Chtholly-img/main/{}.jpg'.format(rd.randint(1, 125))
        rp = rq.get(url=url, headers=head)
        self.send_response(200)
        self.send_header('Content-type', 'application/download')
        self.end_headers()
        self.wfile.write(rp.content)
        return

if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, handler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()