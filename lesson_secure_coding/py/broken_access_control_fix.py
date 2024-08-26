import http.server
import socketserver


TOKEN = 'valid_admin_token'


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/admin":
            if self.headers.get("Authorization") == f"Bearer {TOKEN}":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Welcome to the admin page!")
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Access denied.")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found.")


PORT = 8000
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
