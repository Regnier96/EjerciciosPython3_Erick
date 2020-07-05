import socket as s
import time
from threading import Thread


def recibir(sock):
    contadorDePaquetes = 0
    estaEnviando = False

    while True:
        data, addr = sock.recvfrom(1024)

        if not estaEnviando:
            # Iniciar thread de envio
            e = Thread(target=enviar, args=(sock, addr))
            e.start()

            estaEnviando = True

        contadorDePaquetes += 1
        print(f'[RCV {contadorDePaquetes}] Recibi un mensaje: {data} de {addr}')


def enviar(sock, caddr):

    contadorDePaquetes = 0

    while True:
        if caddr:
            msg = f'Hola {contadorDePaquetes+1}'
            sock.sendto(msg.encode(), caddr)
            print(f'[SND] Paquete {contadorDePaquetes+1} enviado a {caddr}')
            contadorDePaquetes += 1
        else:
            print(f'[SND-ERROR]caddr es {caddr}')

        time.sleep(0.5)


socketServidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
print('Se ha creado el socket del servidor')

ip = ''
port = 8050

socketServidor.bind((ip, port))
print(f'El socket del servidor esta atado a la direccion ip {ip} y el puerto {port}')

# Iniciar thread de recepcion
recibidos = Thread(target=recibir, args=(socketServidor,))

recibidos.start()


