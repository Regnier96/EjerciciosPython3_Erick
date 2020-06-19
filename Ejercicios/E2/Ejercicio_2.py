import re
texto = input("Ingresa una cadena\n")

# No hay letras
noLetras = '[^a-zA-Z]+$'
print("No letras:", True) if re.match(noLetras, texto) else print("No letras:", False)

# Solo Números
soloNumeros = '\d+$'
print("Solo números:", True) if re.match(soloNumeros, texto) else print("Solo números:", False)

# Solo mayusculas
soloMayusculas = '[A-Z]+$'
print("Solo mayúsculas:", True) if re.match(soloMayusculas, texto) else print("Solo mayúsculas:", False)

# Solo minusculas
soloMinusculas = '[a-z]+$'
print("Solo minúsculas:", True) if re.match(soloMinusculas, texto) else print("Solo minusculas:", False)

# No hay numeros
noNumeros = '[^0-9]+$'
print("No números:", True) if re.match(noNumeros, texto) else print("No números:", False)
