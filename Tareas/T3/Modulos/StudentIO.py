try:
    import cPickle as pickle
except ImportError:
    import pickle

import shelve
from Modulos import Ejercicio_3


def guardarEstudiantesP(estudiantes):
    file = open('estudiantes.txt', 'wb')
    pickle.Pickler(file, 4).dump(estudiantes)
    file.close()


def leerEstudiantesP():
    file = open('estudiantes.txt', 'rb')
    unpickler = pickle.Unpickler(file)
    estudiantes = unpickler.load()
    file.close()
    return estudiantes


def guardarEstudiantesS(nombres, correos, contrasenas):
    with shelve.open('estudiantes_shelve') as shelf:
        for nom, co, con in zip(nombres, correos, contrasenas):
            ip = Ejercicio_3.Estudiante(nom, co, con)
            shelf[nom] = ip


def leerEstudiantesS():
    with shelve.open('estudiantes_shelve') as shelf:
        for k in shelf:
            print(f'{k}:\n{shelf[k]}')
            print('\n')
