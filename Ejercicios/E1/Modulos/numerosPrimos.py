def identicarPrimos():
    numero = input("Ingresa un número para saber si es primo\n")
    contador = 0
    try:
        numero = int(numero)
        if numero < 2:
            return "No hay números primos menores a 2"
        for i in range(2, numero + 1):  # Se suma un 1 para que sea posible la comparación entre número e i
            if numero % i == 0:
                contador += 1
        if contador == 1:
            return "Es primo"
        else:
            return "No es primo"
    except ValueError:
        return "No es un dato válido"
