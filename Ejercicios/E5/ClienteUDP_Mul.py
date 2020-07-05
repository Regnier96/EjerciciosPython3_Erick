import socket as s
import time
from threading import Thread


def enviar(sock, saddr):
    contadorDePaquetes = 0

    while True:
        msg = f'Mensaje {contadorDePaquetes+1} de cliente UDP'
        bytes = msg.encode()
        sock.sendto(bytes, saddr)
        print(f'[SND] Paquete {contadorDePaquetes+1} enviado a {addr}')
        contadorDePaquetes += 1
        time.sleep(1)


def recibir(sock):
    contadorDePaquetes = 0

    while True:
        data, addr = sock.recvfrom(1024)
        print(f'[RCV] Recibido [{contadorDePaquetes+1}]: {data} de {addr}')

        contadorDePaquetes += 1


cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)


ip = 'localhost'
port = 8050

addr = ip, port


# Iniciar thread de envio
enviados = Thread(target=enviar, args=(cliente, addr))

time.sleep(3)

# Iniciar thread de recepcion
recibidos = Thread(target=recibir, args=(cliente, ))

enviados.start()
recibidos.start()