import socket

def main():
    mensaje = ""
    print('Cliente 1.0')
    host, port = 'localhost', 8050
    sock = socket.socket()
    sock.connect((host, port))
    while mensaje != 'salir':
        print('Escribe un mensaje o salir para terminar conexion')
        mensaje = input('Usted dice: ')
        sock.send(mensaje.encode())
    sock.close()

main()
