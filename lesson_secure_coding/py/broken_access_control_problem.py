import http.server
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/admin":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome to the admin page!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found.")


PORT = 8000
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
