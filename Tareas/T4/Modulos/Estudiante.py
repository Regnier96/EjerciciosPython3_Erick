from mongoengine import *

class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contrasena = StringField(required=True)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo

    def getContrasena(self):
        return self.contrasena

    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def __str__(self):
        return f'\nNombre: {self.nombre}\n' \
               f'Correo: {self.correo}\n' \
               f'Contraseña: {self.contrasena}'
