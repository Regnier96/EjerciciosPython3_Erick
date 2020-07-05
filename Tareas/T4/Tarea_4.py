from Modulos import BaseDeDatosMongo

coleccion = BaseDeDatosMongo

selector = 0

while selector != 5:
    print('1) Guardar un estudiante')
    print('2) Leer un estudiante')
    print('3) Eliminar un estudiante')
    print('4) Actualizar un estudiante')
    print('5) Salir')
    selector = int(input('Elija una opción\n'))

    if selector == 1:
        nombre = input('Ingresa el nombre del estudiante\n')
        correo = input('Ingresa el correo del estudianten\n')
        contrasena = input('Ingresa la contraseña del estudiante\n')
        coleccion.guardarEstudiante(nombre, correo, contrasena)
    elif selector == 2:
        nombre = input('Introduzca el estudiante a leer\n\n')
        print(coleccion.leerEstudiante(nombre))
        print('\n')

    elif selector == 3:
        nombre = input('Introduzca el estudiante a eliminar\n')
        elimado = coleccion.eliminarEstudiante(nombre)
        if elimado == '':
            print('No es un estudiante registrado')
        else:
            for i in enumerate(elimado):
                print(f'{i}\n')

    elif selector == 4:
        nombre = input('Introduzca el estudiante a modificar\n')
        print(coleccion.modificarEstudiante(nombre))

    else:
        pass
