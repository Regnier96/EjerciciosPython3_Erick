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


def modificarEstudiante(nombre, selector, nuevoN, nuevoCo, nuevaCon):
    estudiantes = Estudiante.Estudiante.objects
    for index, i in enumerate(estudiantes):
        if i.nombre == nombre:
            if selector == 1:
                nom = nuevoN
                Estudiante.Estudiante.update(i, nombre=nom)
                return f'{index} Nombre: {nom}\nCorreo:{i.correo}\nContraseña: {i.contrasena}\n'
            elif selector == 2:
                correo = nuevoCo
                Estudiante.Estudiante.update(i, correo=correo)
                return f'{index} Nombre: {i.nombre}\nCorreo:{correo}\nContraseña: {i.contrasena}\n'
            elif selector == 3:
                contrasena = nuevaCon
                Estudiante.Estudiante.update(i, contrasena=contrasena)
                return f'{index} Nombre: {i.nombre}\nCorreo:{i.correo}\nContraseña: {contrasena}\n'
            elif selector == 4:
                nom = nuevoN
                correo = nuevoCo
                contrasena = nuevaCon
                Estudiante.Estudiante.update(i, nombre=nom, correo=correo, contrasena=contrasena)
                return f'{index} Nombre: {nom}\nCorreo:{correo}\nContraseña: {contrasena}\n'

    return f'{nombre} no es un estudiante registrado\n'

