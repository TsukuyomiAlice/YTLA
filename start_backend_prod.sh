#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

cd "$SCRIPT_DIR/ytla_plan"
export PYTHONPATH="$SCRIPT_DIR"
export FLASK_ENV=production
export FLASK_APP=wsgi:app

echo "============================================="
echo "Starting Flask Backend Server in Production Mode..."
echo "============================================="
echo "Current Directory: $(pwd)"
echo "PYTHONPATH: $PYTHONPATH"
echo "FLASK_ENV: $FLASK_ENV"
echo ""

echo "Checking for gunicorn installation..."
if ! python3 -m pip show gunicorn > /dev/null 2>&1; then
    echo "Installing gunicorn..."
    python3 -m pip install gunicorn
fi

echo "Starting server with gunicorn..."
gunicorn --workers=4 --bind=0.0.0.0:5000 wsgi:app