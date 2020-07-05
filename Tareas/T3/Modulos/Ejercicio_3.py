class Figura:
    def __init__(self, nombre, lados):
        self.__nombre = nombre
        self.__lados = lados

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get__lados(self):
        return self.__lados

    def set__lados(self, lados):
        self.__lados = lados


class Rectangulo(Figura):
    def __init__(self, nombre, lados, perimetro, area):
        super().__init__(nombre, lados)
        self.__perimetro = perimetro
        self.__area = area

    def get_perimetro(self):
        return self.__perimetro

    def set_perimetro(self, perimetro):
        self.__perimetro = perimetro

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def calcular_area(self, base, altura):
        self.__area = base * altura
        return self.__area

    def calcular_perimetro(self, base, altura):
        self.__perimetro = (base * 2) + (altura * 2)
        return self.__perimetro


class Triangulo(Figura):
    def __init__(self, nombre, lados, perimetro, area):
        super().__init__(nombre, lados)
        self.__perimetro = perimetro
        self.__area = area

    def get_perimetro(self):
        return self.__perimetro

    def set_perimetro(self, perimetro):
        self.__perimetro = perimetro

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def calcular_area(self, base, altura):
        self.__area = (base * altura) / 2
        return self.__area

    def calcular_perimetro(self, lado1, lado2, lado3):
        self.__perimetro = lado1 + lado2 + lado3
        return self.__perimetro


class Estudiante():
    __nombre = ''
    __correo = ''
    __contrasena = ''

    def __init__(self, nombre, correo, contrasena):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo

    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def __str__(self):
        return f'Nombre: {self.__nombre}\n' \
               f'Correo: {self.__correo}\n' \
               f'Contraseña: {self.__contrasena}'
