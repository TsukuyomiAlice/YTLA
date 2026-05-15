#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

cd "$SCRIPT_DIR/ytla_plan_vue"

if [ ! -d "dist" ]; then
    echo "dist directory not found, building frontend..."
    npm install
    npm run build
fi

cd dist

echo "Starting static file server on port 5173..."
python3 -c "
import http.server
import socketserver
import os

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

os.chdir('.')
PORT = 5173
with socketserver.TCPServer(('0.0.0.0', PORT), MyHTTPRequestHandler) as httpd:
    print(f'Serving at http://localhost:{PORT}')
    httpd.serve_forever()
"