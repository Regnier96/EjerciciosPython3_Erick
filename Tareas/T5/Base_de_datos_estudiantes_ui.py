# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Base_de_datos_estudiantes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 613)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.Nombre = QLineEdit(self.groupBox)
        self.Nombre.setObjectName(u"Nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Nombre)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.Correo = QLineEdit(self.groupBox)
        self.Correo.setObjectName(u"Correo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Correo)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.Contrasena = QLineEdit(self.groupBox)
        self.Contrasena.setObjectName(u"Contrasena")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Contrasena)

        self.Boton_Registrar = QPushButton(self.groupBox)
        self.Boton_Registrar.setObjectName(u"Boton_Registrar")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Boton_Registrar)


        self.horizontalLayout.addWidget(self.groupBox)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.actualizarContrasena = QLineEdit(self.centralwidget)
        self.actualizarContrasena.setObjectName(u"actualizarContrasena")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.actualizarContrasena)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.Boton_Actualizar = QPushButton(self.centralwidget)
        self.Boton_Actualizar.setObjectName(u"Boton_Actualizar")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.Boton_Actualizar)

        self.Boton_Leer = QPushButton(self.centralwidget)
        self.Boton_Leer.setObjectName(u"Boton_Leer")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.Boton_Leer)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.BuscarEdit = QLineEdit(self.centralwidget)
        self.BuscarEdit.setObjectName(u"BuscarEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.BuscarEdit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.actualizarNombre = QLineEdit(self.centralwidget)
        self.actualizarNombre.setObjectName(u"actualizarNombre")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.actualizarNombre)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.actualizarCorreo = QLineEdit(self.centralwidget)
        self.actualizarCorreo.setObjectName(u"actualizarCorreo")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.actualizarCorreo)


        self.horizontalLayout.addLayout(self.formLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Boton_Eliminar = QPushButton(self.centralwidget)
        self.Boton_Eliminar.setObjectName(u"Boton_Eliminar")

        self.verticalLayout.addWidget(self.Boton_Eliminar)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 657, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contase\u00f1a", None))
        self.Boton_Registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contase\u00f1a", None))
        self.Boton_Actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.Boton_Leer.setText(QCoreApplication.translate("MainWindow", u"Leer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.Boton_Eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

