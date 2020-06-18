def identifcarNumero():
    numero = input("Ingresa un número para saber si es par o impar\n")
    try:
        numero = int(numero)
        if numero % 2 == 0:
            return "Es par"
        else:
            return "Es impar"
    except ValueError:
        return "No es un dato válido"
