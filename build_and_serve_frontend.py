#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import http.server
import socketserver

def run_command(cmd, cwd=None):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: Command failed with exit code {result.returncode}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        return False
    print(f"Success!")
    return True

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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(script_dir, 'ytla_plan_vue')
    dist_dir = os.path.join(frontend_dir, 'dist')
    port = 5173
    
    print("=" * 60)
    print("YTLA Frontend Production Server")
    print("=" * 60)
    print(f"Script Directory: {script_dir}")
    print(f"Frontend Directory: {frontend_dir}")
    print(f"Dist Directory: {dist_dir}")
    print("=" * 60)
    
    if not os.path.exists(frontend_dir):
        print(f"ERROR: Frontend directory not found: {frontend_dir}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    os.chdir(frontend_dir)
    print(f"\n[1/5] Current working directory: {os.getcwd()}")
    
    print("\n[2/5] Cleaning existing dist directory...")
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
        print(f"Removed existing dist directory")
    else:
        print("No existing dist directory to clean")
    
    print("\n[3/5] Installing dependencies...")
    if not run_command("npm install"):
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n[4/5] Building frontend...")
    if not run_command("npm run build"):
        input("Press Enter to exit...")
        sys.exit(1)
    
    if not os.path.exists(dist_dir):
        print(f"\nERROR: Build failed, dist directory not created")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n[5/5] Starting static server on port {port}...")
    print(f"Changing to dist directory: {dist_dir}")
    os.chdir(dist_dir)
    print(f"Current directory: {os.getcwd()}")
    
    with socketserver.TCPServer(('0.0.0.0', port), MyHTTPRequestHandler) as httpd:
        print(f"\n✓ Server is running at: http://localhost:{port}")
        print("✓ Serving files from: " + dist_dir)
        print("\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    main()