from Modulos import Validacion

correo1 = input("Ingresa tu correo de una extension\n")
print(True if Validacion.validarCorreoUnaExtension(correo1) else False)

correo2 = input("Ingresa tu correo de dos extensiones\n")
print(True if Validacion.validarCorreoDosExtensiones(correo2) else False)

telefono1 = input("Ingresa tu numero telefonico de 10 digitos\n")
print("Numero valido:", "Sí" if Validacion.validarNumeroTelefonico(telefono1) else "No")

telefono2 = input("Ingresa tu (lada) y numero telefonico\n")
print("Numero valido:", "Si" if Validacion.validarNumeroTelefonicoLada(telefono2) else "No")

rfc = input("Ingresa tu RFC\n")
print("RFC valido:", "Si" if Validacion.validarRFC(rfc) else "No")

curp = input("Ingresa tu curp\n")
print("Curp valido:", "Si" if Validacion.validarCURP(curp) else "No")

