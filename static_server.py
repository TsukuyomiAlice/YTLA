#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith('.ts'):
            return 'application/javascript'
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.html'):
            return 'text/html'
        if path.endswith('.json'):
            return 'application/json'
        if path.endswith('.svg'):
            return 'image/svg+xml'
        if path.endswith('.ico'):
            return 'image/x-icon'
        return super().guess_type(path)

def main():
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5173
    
    print(f"Starting static file server on port {port}...")
    with socketserver.TCPServer(('0.0.0.0', port), MyHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()

if __name__ == '__main__':
    main()