def comprobarAño():
    anio = input("Ingrese un año para saber si es bisiesto\n")
    try:
        anio = int(anio)
        if anio % 4 == 0 or (anio % 100 == 0 and anio % 400 == 0):
            return f"{anio} es bisiesto"
        else:
            return f"{anio} no es bisiesto"
    except ValueError:
        return "Valor no valido"


