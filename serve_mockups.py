#!/usr/bin/env python3
"""
High-performance threaded HTTP server for ParkSpot mockups.
- Binds to 0.0.0.0 (all IPv4 interfaces)
- Supports multithreading (ThreadingHTTPServer) to prevent hangs
- Adds CORS (Access-Control-Allow-Origin: *)
- Serves on port 8765 and optionally port 8000
"""

import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SERVE_DIR = Path(__file__).resolve().parent

class RobustHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SERVE_DIR), **kwargs)

    def end_headers(self):
        # Allow CORS for port-forwarded and cross-origin previews
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # Compact log output
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

def start_server_on_port(port):
    try:
        server = ThreadingHTTPServer(("0.0.0.0", port), RobustHandler)
        print(f"Serving {SERVE_DIR} on http://0.0.0.0:{port} (ThreadingHTTPServer active)")
        server.serve_forever()
    except Exception as e:
        print(f"Could not start server on port {port}: {e}")

if __name__ == "__main__":
    ports = [8765, 8000]
    threads = []
    
    # Start port 8765 on main thread, and port 8000 in background thread
    t8000 = threading.Thread(target=start_server_on_port, args=(8000,), daemon=True)
    t8000.start()
    
    start_server_on_port(8765)
