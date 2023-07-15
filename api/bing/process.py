from http.server import *
import requests as rq
import json
from PIL import Image, ImageFilter
from urllib.parse import urlparse, parse_qs
import io

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        rp = rq.get(url='https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        dt = rp.json()
        url = 'https://cn.bing.com' + dt['images'][0]['url']
        rp = rq.get(url)
        img = Image.open(io.BytesIO(rp.content))
        rad = int(parse_qs(urlparse(self.path).query).get('blurRadius', ['0'])[0])
        img = img.filter(ImageFilter.GaussianBlur(radius = rad))
        img_byte = io.BytesIO()
        img.save(img_byte, format='JPEG')
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        self.wfile.write(img_byte.getvalue())
        return

if __name__ == '__main__':
    host = ('127.0.0.1', 8000)
    server = HTTPServer(host, handler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()