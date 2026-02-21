#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
from functools import partial
import sys
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def translate_path(self, path):
        # Strip the /mahabharata/ prefix so files are served from the project root
        prefix = '/mahabharata/'
        if path.startswith(prefix):
            path = '/' + path[len(prefix):]
        elif path == '/mahabharata':
            path = '/'
        return super().translate_path(path)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"Serving at http://localhost:{port}/mahabharata/")
    test(CORSRequestHandler, HTTPServer, bind="0.0.0.0", port=port)
