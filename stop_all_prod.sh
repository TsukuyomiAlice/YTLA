#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

echo "============================================="
echo "Stopping All Production Servers..."
echo "============================================="

if [ -f "$SCRIPT_DIR/backend_prod.pid" ]; then
    BACKEND_PID=$(cat "$SCRIPT_DIR/backend_prod.pid")
    echo "Stopping Backend Server (PID: $BACKEND_PID)..."
    kill $BACKEND_PID 2>/dev/null || true
    rm "$SCRIPT_DIR/backend_prod.pid"
    echo "Backend Server stopped."
fi

if [ -f "$SCRIPT_DIR/frontend_prod.pid" ]; then
    FRONTEND_PID=$(cat "$SCRIPT_DIR/frontend_prod.pid")
    echo "Stopping Frontend Server (PID: $FRONTEND_PID)..."
    kill $FRONTEND_PID 2>/dev/null || true
    rm "$SCRIPT_DIR/frontend_prod.pid"
    echo "Frontend Server stopped."
fi

if command -v nginx > /dev/null 2>&1; then
    echo "Stopping nginx..."
    sudo nginx -s stop 2>/dev/null || true
    echo "Nginx stopped."
fi

echo "============================================="
echo "All production servers stopped."
echo "============================================="