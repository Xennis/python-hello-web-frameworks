import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):

    __CUSTOMER_INFO_ROUTE = r"/customer/([a-zA-Z0-9\-]+)/info"

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(json.dumps({"Hello": "World"}).encode())
        elif re.match(self.__CUSTOMER_INFO_ROUTE, self.path):
            customer_id = re.match(self.__CUSTOMER_INFO_ROUTE, self.path)[1]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(json.dumps({"customer_id": customer_id}).encode())
        else:
            self.send_response(404)


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, Server)
    print(f"Starting httpd server on http://localhost:8000/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
