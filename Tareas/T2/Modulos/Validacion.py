import re

# Validador de correo de un dominio
def validarCorreoUnaExtension(cadena):
    patron = '[^@]+@[^@]+\.[^@\.]{2,4}$'
    if re.match(patron, cadena):
        return True
    else:
        return False

def validarCorreoDosExtensiones(cadena):
    patron = '[^@]+@[^@]+\.[^@]+\.[^@]{2,4}$'
    if re.match(patron, cadena):
        return True
    else:
        return False

def validarNumeroTelefonico(cadena):
    patron = '\d{10}$'
    if re.match(patron ,cadena):
        return True
    else:
        return False

def validarNumeroTelefonicoLada(cadena):
    patron1 = '[\(](\d{2})[\)][\s](\d{4})[\s](\d{4})'
    patron2 = '[\(](\d{2})[\)][\-](\d{4})[\-](\d{4})'
    patron3 = '[\(](\d{3})[\)][\s](\d{3})[\s](\d{4})'
    patron4 = '[\(](\d{3})[\)][\-](\d{3})[\-](\d{4})'
    if re.match(patron1, cadena):
        return True
    elif re.match(patron2, cadena):
        return True
    elif re.match(patron3, cadena):
        return True
    elif re.match(patron4, cadena):
        return True
    else:
        return False

def validarRFC(cadena):
    patron = '[A-Z]{4}(\d{6})(\w{3})$'
    if re.match(patron, cadena):
        return True
    else:
        return False

def validarCURP(cadena):
    patron = '[A-Z]{4}(\d{6})(H|M)[A-Z]{5}(\d|[A-Z])(\d)$'
    if re.match(patron, cadena):
        return True
    else:
        return False
