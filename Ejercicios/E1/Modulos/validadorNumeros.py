def validarNumero():
    numero = input("Ingresa un numero para saber si es positivo, cero o negativo\n")
    try:
        numero = float(numero)
        if numero == 0:
            return "El valor es cero"
        elif numero > 0:
            return "El valor es positivo"
        else:
            return "El número es negativo"
    except ValueError:
        return "Dato no valido"
