import socket


class ClienteUDP:
    __socket = None
    __paquetesEnviados = 0
    __paquetesRecibidos = 0

    def __init__(self, ip, puerto):
        self.__socket = socket.socket()
        self.__socket.connect((ip, puerto))

        salir = False

        while not salir:
            print('Escribe un mensaje (Quit para salir):')
            entrada = input()

            self.enviar(entrada, (ip, puerto))

            rcv = self.recibir()
            print(f'[RCV: {self.__paquetesRecibidos}] {rcv}')

            if entrada == 'Quit':
                salir = True
                print('Saliendo ...')
                continue

    def enviar(self, mensaje, addr):
        self.__paquetesEnviados += 1
        print(f'[SND:{self.__paquetesEnviados}] {mensaje}')
        self.__socket.send(mensaje.encode(), addr)

    def recibir(self):
        data, addr = self.__socket.recv(1024)
        self.__paquetesRecibidos += 1
        return data.decode(), addr
