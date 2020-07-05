from mongoengine import *
from Modulos import Estudiante

connect('padts')

def guardarEstudiante(nombre, correo, contrasena):
    estudiante = Estudiante.Estudiante()
    estudiante.setNombre(nombre)
    estudiante.setCorreo(correo)
    estudiante.setContrasena(contrasena)
    estudiante.save()


def leerEstudiante(nombres):
    estudiantes = Estudiante.Estudiante.objects
    lista = []
    for index, i in enumerate(estudiantes):
        if i.nombre == nombres:
            lista.insert(index, i)
    return lista


def eliminarEstudiante(nombre):
    estudiantes = Estudiante.Estudiante.objects
    for index, i in enumerate(estudiantes):
        if i.nombre == nombre:
            Estudiante.Estudiante.delete(i)
            estudiantes = Estudiante.Estudiante.objects
            return estudiantes

    return ''


def modificarEstudiante(nombre):
    estudiantes = Estudiante.Estudiante.objects
    for index, i in enumerate(estudiantes):
        if i.nombre == nombre:
            print('1) Modificar nombre')
            print('2) Modificar correo')
            print('3) Modificar contraseña')
            print('4) Modificar todo')
            selector = int(input('Selecciona una opcion\n'))
            if selector == 1:
                nom = input('Introduce el nuevo nombre\n')
                Estudiante.Estudiante.update(i, nombre=nom)
                return f'{index} Nombre: {nom}\nCorreo:{i.correo}\nContraseña: {i.contrasena}\n'
            elif selector == 2:
                correo = input('Introduce el nuevo correo\n')
                Estudiante.Estudiante.update(i, correo=correo)
                return f'{index} Nombre: {i.nombre}\nCorreo:{correo}\nContraseña: {i.contrasena}\n'
            elif selector == 3:
                contrasena = input('Introduce la nueva contraseña\n')
                Estudiante.Estudiante.update(i, contrasena=contrasena)
                return f'{index} Nombre: {i.nombre}\nCorreo:{i.correo}\nContraseña: {contrasena}\n'
            elif selector == 4:
                nom = input('Introduce el nuevo nombre\n')
                correo = input('Introduce el nuevo correo\n')
                contrasena = input('Introduce la nueva contraseña\n')
                Estudiante.Estudiante.update(i, nombre=nom, correo=correo, contrasena=contrasena)
                return f'{index} Nombre: {nom}\nCorreo:{correo}\nContraseña: {contrasena}\n'

    return f'{nombre} no es un estudiante registrado\n'

