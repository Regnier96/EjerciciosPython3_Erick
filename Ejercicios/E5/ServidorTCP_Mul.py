import socketserver
import threading
import time

class ServidorTCP(socketserver.BaseRequestHandler):
    def handle(self):
        data = ""
        while data != "salir":
            data = self.request.recv(1024).decode()
            print(data)
            time.sleep(0.1)


class ThreadServer (socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    host = 'localhost'
    port = 8050
    server = ThreadServer((host, port), ServidorTCP)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print('Server corriendo...')

main()
