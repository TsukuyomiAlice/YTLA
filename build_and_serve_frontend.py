#!/usr/bin/env python3
import os
import sys
import subprocess
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
    current_dir = os.getcwd()
    print(f"\n[1/4] Current working directory: {current_dir}")
    
    if not os.path.exists(dist_dir):
        print("\n[2/4] dist directory not found, starting build...")
        
        print("\nInstalling dependencies...")
        if not run_command("npm install"):
            input("Press Enter to exit...")
            sys.exit(1)
        
        print("\nBuilding frontend...")
        if not run_command("npm run build"):
            input("Press Enter to exit...")
            sys.exit(1)
    else:
        print("\n[2/4] dist directory already exists, skipping build")
    
    if not os.path.exists(dist_dir):
        print(f"\nERROR: Build failed, dist directory not created")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n[3/4] Checking dist/index.html...")
    index_path = os.path.join(dist_dir, 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'src="/src/main.ts"' in content:
                print("WARNING: index.html still references src/main.ts!")
                print("Build may have issues.")
            else:
                print("OK: index.html references look correct")
                # Show script tags
                for line in content.split('\n'):
                    if 'script' in line:
                        print(f"  {line.strip()}")
    else:
        print(f"ERROR: {index_path} not found")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print(f"\n[4/4] Starting static server on port {port}...")
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