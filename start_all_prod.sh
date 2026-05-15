#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

echo "============================================="
echo "Starting All Servers in Production Mode..."
echo "============================================="

echo "Step 1: Starting backend server in background..."
cd "$SCRIPT_DIR/ytla_plan"
export PYTHONPATH="$SCRIPT_DIR"
export FLASK_ENV=production

if ! python3 -m pip show gunicorn > /dev/null 2>&1; then
    python3 -m pip install gunicorn
fi

nohup gunicorn --workers=4 --bind=0.0.0.0:5000 wsgi:app > backend_prod.log 2>&1 &
BACKEND_PID=$!
echo "Backend Server started with PID: $BACKEND_PID"
echo "$BACKEND_PID" > "$SCRIPT_DIR/backend_prod.pid"

sleep 3

echo ""
echo "Step 2: Building frontend if needed..."
cd "$SCRIPT_DIR/ytla_plan_vue"
if [ ! -d "dist" ]; then
    echo "Building frontend..."
    npm install
    npm run build
fi

echo ""
echo "Step 3: Starting frontend static server in background..."
cd dist
nohup python3 -c "
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

PORT = 5173
with socketserver.TCPServer(('0.0.0.0', PORT), MyHTTPRequestHandler) as httpd:
    httpd.serve_forever()
" > frontend_prod.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend Server started with PID: $FRONTEND_PID"
echo "$FRONTEND_PID" > "$SCRIPT_DIR/frontend_prod.pid"

echo ""
echo "============================================="
echo "Servers started successfully!"
echo "- Backend API: http://localhost:5000"
echo "- Frontend: http://localhost:5173"
echo "============================================="