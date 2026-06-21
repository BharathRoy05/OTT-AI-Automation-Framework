"""Local demo OTT app server for running the automation framework without a real URL."""

from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


HOST = "127.0.0.1"
PORT = 8000
APP_DIR = Path(__file__).parent


class DemoAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def do_GET(self) -> None:
        if self.path.startswith(("/login", "/home", "/search", "/watch", "/account/subscription")):
            self.path = "/index.html"
        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), DemoAppHandler)
    print(f"Demo OTT app running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()
