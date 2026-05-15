#!/bin/bash
SCRIPT_DIR="$(dirname "$0")"

cd "$SCRIPT_DIR/ytla_plan_vue"

echo "============================================="
echo "Building Vue Frontend for Production..."
echo "============================================="
echo "Current Directory: $(pwd)"
echo ""

echo "Installing dependencies..."
npm install

echo ""
echo "Building..."
npm run build

echo ""
echo "Build completed! Output in dist/ directory."