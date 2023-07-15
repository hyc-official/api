from http.server import *
import requests as rq
import json
from PIL import Image, ImageFilter
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        rp = rq.get(url='https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        dt = rp.json()
        url = 'https://cn.bing.com' + dt['images'][0]['url']
        rp = rq.get(url=url)
        pth = "temp.jpg"
        with open(pth, "wb+") as f:
            f.write(rp.content)
        img = Image.open(pth)
        rad = int(parse_qs(urlparse(self.path).query).get("blurRadius")[0])
        img = img.filter(ImageFilter.GaussianBlur(radius = rad))
        img.save(pth)
        with open(pth, "rb") as f:
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(f.read())
        return

if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, handler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()