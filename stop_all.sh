#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

echo "============================================="
echo "Stopping All Servers..."
echo "============================================="

if [ -f "$SCRIPT_DIR/backend.pid" ]; then
    BACKEND_PID=$(cat "$SCRIPT_DIR/backend.pid")
    echo "Stopping Backend Server (PID: $BACKEND_PID)..."
    kill $BACKEND_PID 2>/dev/null || true
    rm "$SCRIPT_DIR/backend.pid"
    echo "Backend Server stopped."
fi

if [ -f "$SCRIPT_DIR/frontend.pid" ]; then
    FRONTEND_PID=$(cat "$SCRIPT_DIR/frontend.pid")
    echo "Stopping Frontend Server (PID: $FRONTEND_PID)..."
    kill $FRONTEND_PID 2>/dev/null || true
    rm "$SCRIPT_DIR/frontend.pid"
    echo "Frontend Server stopped."
fi

echo "============================================="
echo "All servers stopped."
echo "============================================="