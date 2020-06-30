import socket

class ClienteTCP:

    __socket = None
    __paquetesRecibidos = 0
    __paquetesEnviados = 0

    def __init__(self, ip, puerto):
        self.__socket = socket.socket()
        self.__socket.connect((ip, puerto))
        print('Conectando al servidor')

        salir = False

        while not salir:
            entrada = input('Escribe un mensaje (Salir para terminar la conexion):\n')

            self.enviar(entrada)
            recibido = self.recibir()

            if recibido == b'':
                salir = True
                print('Saliendo...')
            else:
                print(f'[RCV: {self.__paquetesRecibidos}] {recibido}')

        self.__socket.close()
        print('Conexion cerrada')



    def recibir(self):
        paquete = self.__socket.recv(1024).decode()
        self.__paquetesRecibidos += 1
        return paquete.__str__()



    def enviar(self, mensaje):
        self.__paquetesEnviados += 1
        print(f'[SND:{self.__paquetesEnviados}] {mensaje.encode()}')
        self.__socket.send(mensaje.encode())
