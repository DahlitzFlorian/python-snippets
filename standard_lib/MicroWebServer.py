import socket
import threading
import os.path
import re

HTTPVER = "HTTP/1.1"
SERVER = "PythonMicroWebServer/0.1"
LINEBREAK = "\r\n"


class WebServer(object):
    def __init__(self, hostname="", port=80, document_root="./"):
        self._connectionHandler = WebServer.ConnectionHandler(
            hostname, port, document_root
        )

    def server_forever(self):
        self._connectionHandler.start()

    def clean_exit(self):
        self._connectionHandler.stop()

    def route(self, path, **options):
        def decorator(func):
            self._connectionHandler.routes.append((path, func))

        return decorator

    class ConnectionHandler(threading.Thread):
        def __init__(self, hostname, port, document_root):
            self._hostname = hostname
            self._port = port
            self._document_root = document_root

            self.routes = []

            self.running = False

            threading.Thread.__init__(self)

        def stop(self):
            self.running = False

        def run(self):
            self.running = True

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self._hostname, self._port))
            sock.listen(1)

            while self.running:
                client, address = sock.accept()

                raw_data = client.recv(1024)

                if not raw_data:
                    continue

                http_request = WebServer.HTTPRequest.parse(raw_data)

                print(
                    "%s [%s] requested %s%s"
                    % (
                        address[0],
                        http_request.header["User-Agent"],
                        http_request.host,
                        http_request.uri,
                    )
                )

                file = http_request.uri

                if file in [x[0] for x in self.routes]:
                    for x in self.routes:
                        if x[0] == file:
                            x[1](client)
                            break
                    continue

                if os.path.isfile(self._document_root + file):
                    with open(self._document_root + file, "rb") as f:
                        http_response = WebServer.HTTPResponse(
                            f.read(),
                            content_type=WebServer.HTTPResponse.file_extension_to_content_type(
                                file.split(".")[-1]
                            ),
                        )
                        f.close()

                elif os.path.isfile(self._document_root + "error404.html"):
                    with open(self._document_root + "error404.html", "rb") as f:
                        http_response = WebServer.HTTPResponse(
                            f.read(), code="404 NOT FOUND"
                        )
                        f.close()

                else:
                    http_response = WebServer.HTTPResponse(
                        "<h1>404 Not Found</h1><h2>404 Error not found...</h2>",
                        code="404 NOT FOUND",
                    )

                client.send(http_response.raw)
                client.close()

            sock.close()

    class HTTPRequest(object):
        def __init__(self, http_ver, host, request_type, uri, header):
            self.http_ver = http_ver
            self.host = host
            self.request_type = request_type
            self.uri = uri
            self.header = header

        @staticmethod
        def parse(data):
            data = data.decode("utf-8")
            lines = data.splitlines()

            request_type, uri, http_ver = lines[0].split()

            header = {}

            for h in lines:
                h = h.split(": ")

                if len(h) < 2:
                    continue

                field = h[0]
                value = h[1]

                header[field] = value

            host = header["Host"]

            if "?" in uri:
                uri = uri.split("?")[0]

            print(uri)

            if uri.endswith("/"):
                uri += "index.html"

            return WebServer.HTTPRequest(http_ver, host, request_type, uri, header)

    class HTTPResponse(object):
        def __init__(self, body, content_type="text/html", code="200 OK"):
            response = HTTPVER + " " + code + LINEBREAK
            response += "SERVER: " + SERVER + LINEBREAK
            response += "Connection: close" + LINEBREAK
            response += "Content-Type: " + content_type + LINEBREAK
            response += LINEBREAK

            response = response.encode("utf-8")
            self.header = response

            if type(body) == str:
                response += body.encode("utf-8")
            else:
                response += body

            self.body = body
            self.content_type = content_type
            self.code = code

            self.raw = response

        @staticmethod
        def file_extension_to_content_type(file_extension):
            if file_extension in ["html", "htm"]:
                return "text/html"
            if file_extension in ["js"]:
                return "text/javascript"
            if file_extension in ["css"]:
                return "text/css"

            if file_extension in ["jpeg", "jpg", "jpe"]:
                return "image/jpeg"
            if file_extension in ["png"]:
                return "image/png"
            if file_extension in ["ico"]:
                return "image/x-ico"
            if file_extension in ["gif"]:
                return "image/gif"
            if file_extension in ["cod"]:
                return "image/cis-cod"
            if file_extension in ["ras"]:
                return "image/cmu-raster"
            if file_extension in ["fif"]:
                return "image/fif"
            if file_extension in ["ief"]:
                return "image/ief"
            if file_extension in ["tiff", "tif"]:
                return "image/tiff"
            if file_extension in ["mcf"]:
                return "image/vasa"
            if file_extension in ["wbmp"]:
                return "image/vnd.wap.wbmp"
            if file_extension in ["fh4", "fh5", "fhc"]:
                return "image/x-freehand"
            if file_extension in ["pnm"]:
                return "image/x-portable-anymap"
            if file_extension in ["pbm"]:
                return "image/x-portable-bitmap"
            if file_extension in ["pgm"]:
                return "image/x-portable-graymap"
            if file_extension in ["ppm"]:
                return "image/x-portable-pixmap"
            if file_extension in ["rgb"]:
                return "image/x-rgb"
            if file_extension in ["xwd"]:
                return "image/x-windowdump"
            if file_extension in ["xbm"]:
                return "image/x-bitmap"
            if file_extension in ["xpm"]:
                return "image/x-pixmap"

            if file_extension in ["wmv"]:
                return "video/x-ms-wmv"
            if file_extension in ["avi"]:
                return "video/x-msvideo"
            if file_extension in ["mpeg", "mpg", "mpe"]:
                return "video/mpeg"
            if file_extension in ["qt", "mov"]:
                return "video/quicktime"
            if file_extension in ["viv", "vivo"]:
                return "video/vnd.vivo"
            if file_extension in ["movie"]:
                return "video/x-sgi-movie"

            return "application/octet-stream"


if __name__ == "__main__":
    webserver = WebServer(document_root="./web/")

    @webserver.route("/*")
    def data(client):
        http_response = WebServer.HTTPResponse("<h1>hallo pual :o</h1>")
        client.send(http_response.raw)
        client.close()

    webserver.server_forever()
    input("Press any key to stop...")
    webserver.clean_exit()
