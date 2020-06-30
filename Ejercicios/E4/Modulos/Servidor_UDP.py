import socket

class ServidorUDP:
    __socketServidor = None

    __paquetesEnviados = 0
    __paquetesRecibidos = 0

    def __init__(self, puerto):
        self.__socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socketServidor.bind(('', puerto))

        salir = False

        while not salir:
            recibido, direccion = self.recibir()

            if recibido == 'Quit':
                mensaje = f'[RCV: {self.__paquetesRecibidos}]: "{recibido}" from {direccion}. Cerrando socket ...'
                salir = True
            else:
                mensaje = f'[RCV: {self.__paquetesRecibidos}]: "{recibido}" from {direccion}'

            self.enviar(mensaje, direccion)

        self.__socketServidor.close()

    def enviar(self, mensaje, addr):
        self.__paquetesEnviados += 1
        print(f'[SND:{self.__paquetesEnviados}] {mensaje}')
        self.__socketServidor.sendto(mensaje.encode(), addr)

    def recibir(self):
        dato, direccion = self.__socketServidor.recvfrom(1024)
        self.__paquetesRecibidos += 1
        return dato.decode(), direccion
