#!/bin/bash
cd "$(dirname "$0")/ytla_plan"
export PYTHONPATH="$(dirname "$0")"
echo "Starting Flask Backend Server..."
echo "Current Directory: $(pwd)"
echo "PYTHONPATH: $PYTHONPATH"
python3 app.py