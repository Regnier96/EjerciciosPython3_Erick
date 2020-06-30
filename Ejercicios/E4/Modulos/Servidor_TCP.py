import socket

class ServidorTCP:
    __clienteSocket = None
    __clienteDireccion = None
    __paquetesRecibidos = 0
    __paquetesEnviados = 0

    def __init__(self, puerto):
        self.__socketServidor = socket.socket()
        self.__socketServidor.bind(('', puerto))
        self.__socketServidor.listen()
        self.__clienteSocket, self.__clienteDireccion = self.__socketServidor.accept()

        salir = False

        while not salir:
            recibido = self.recibir
            if recibido == 'Salir':
                mensaje = f'[RCV: {self.__paquetesRecibidos}]: cerrando conexion ...'
                salir = True
            else:
                mensaje = f'[RCV: {self.__paquetesRecibidos}]: '
            self.enviar(mensaje)

        self.__clienteSocket.close()
        self.__socketServidor.close()
        print('Conexiones cerradas')


    def recibir(self):
        self.__paquetesRecibidos += 1
        recibido = self.__clienteSocket.recv(1024)
        return recibido

    def enviar(self, mensaje):
        self.__paquetesEnviados += 1
        print(f'[SND: {self.__paquetesEnviados}] {mensaje.encode()}')
        self.__clienteSocket.send(mensaje.encode())
