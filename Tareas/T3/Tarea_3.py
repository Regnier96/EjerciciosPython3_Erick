from Modulos import Ejercicio_3
from Modulos import StudentIO

nombres = ['Erick', 'Oscar', 'Pedro', 'Jessica', 'Juan']
correos = ['eick@gmail.com', 'oscar@gmail.com', 'pedro@gmail.com', 'jessica@gmail.com', 'juan@gmail.com']
contrasenas = ['erick96', 'oscar93', 'pedroHO', 'jessicaAB98', 'juan89566sd']

estudiantes = []

for nom, co, con in zip(nombres, correos, contrasenas):
    estudiantes.append(Ejercicio_3.Estudiante(nom, co, con))


StudentIO.guardarEstudiantesP(estudiantes)
for i in StudentIO.leerEstudiantesP():
    print(i)

StudentIO.guardarEstudiantesS(nombres, correos, contrasenas)
print (StudentIO.leerEstudiantesS())


