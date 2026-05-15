#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

echo "============================================="
echo "Starting All Servers..."
echo "============================================="

echo "Starting Flask Backend Server in background..."
cd "$SCRIPT_DIR/ytla_plan"
export PYTHONPATH="$SCRIPT_DIR"
nohup python3 app.py > backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend Server started with PID: $BACKEND_PID"
echo "Logs: $SCRIPT_DIR/ytla_plan/backend.log"

sleep 3

echo "Starting Vue Frontend Server in background..."
cd "$SCRIPT_DIR/ytla_plan_vue"
nohup npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend Server started with PID: $FRONTEND_PID"
echo "Logs: $SCRIPT_DIR/ytla_plan_vue/frontend.log"

echo ""
echo "============================================="
echo "Servers started successfully!"
echo "- Backend: http://localhost:5000"
echo "- Frontend: http://localhost:5173"
echo ""
echo "To stop servers:"
echo "  kill $BACKEND_PID $FRONTEND_PID"
echo "Or run: ./stop_all.sh"
echo "============================================="

echo "$BACKEND_PID" > "$SCRIPT_DIR/backend.pid"
echo "$FRONTEND_PID" > "$SCRIPT_DIR/frontend.pid"