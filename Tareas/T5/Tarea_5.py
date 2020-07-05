import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from Modulos import BaseDeDatosMongo
from PySide2.QtCore import Slot
from Base_de_datos_estudiantes_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = BaseDeDatosMongo

        self.ui.Boton_Registrar.clicked.connect(self.registrar)
        self.ui.Boton_Leer.clicked.connect(self.leer)
        self.ui.Boton_Eliminar.clicked.connect(self.eliminar)
        self.ui.Boton_Actualizar.clicked.connect(self.actualizar)

    @Slot()
    def registrar(self):
        nombre = self.ui.Nombre.text()
        correo = self.ui.Correo.text()
        contrasena = self.ui.Contrasena.text()
        self.db.guardarEstudiante(nombre, correo, contrasena)
        self.ui.Nombre.clear()
        self.ui.Correo.clear()
        self.ui.Contrasena.clear()

    @Slot()
    def leer(self):
        self.ui.textEdit.clear()
        nombre = self.ui.BuscarEdit.text()
        estudiantes = self.db.leerEstudiante(nombre)
        if estudiantes == []:
            self.ui.textEdit.append('No se encontró al estudiante')
        else:
            self.ui.textEdit.append(estudiantes.__str__())


    @Slot()
    def eliminar(self):
        nombre = self.ui.BuscarEdit.text()
        eliminado = self.db.eliminarEstudiante(nombre)
        if eliminado == '':
            self.ui.textEdit.append('No es un estudiante registrado')
        else:
            for i in enumerate(eliminado):
                self.ui.textEdit.append(f'{i}\n')

    @Slot()
    def actualizar(self):
        self.ui.textEdit.clear()
        comparador = self.ui.BuscarEdit.text()
        nombre = self.ui.actualizarNombre.text()
        correo = self.ui.actualizarCorreo.text()
        contrasena = self.ui.actualizarContrasena.text()

        if nombre and correo and contrasena:
            self.ui.textEdit.append(self.db.modificarEstudiante(comparador, 4, nombre, correo, contrasena))
        elif nombre:
            self.ui.textEdit.append(self.db.modificarEstudiante(comparador, 1, nombre, None, None))
        elif correo:
            self.ui.textEdit.append(self.db.modificarEstudiante(comparador, 2, None, correo, None))
        elif contrasena:
            self.ui.textEdit.append(self.db.modificarEstudiante(comparador, 3, None , None, contrasena))



if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
