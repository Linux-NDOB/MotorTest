# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desktop_app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Mq(object):
    def setupUi(self, Mq):
        if not Mq.objectName():
            Mq.setObjectName(u"Mq")
        Mq.resize(640, 486)
        self.centralwidget = QWidget(Mq)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 641, 461))
        self.label.setPixmap(QPixmap(u"assets/material-design-wallpaper-10.png"))
        self.label.setScaledContents(True)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 110, 581, 341))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 50, 231, 16))
        self.label_5.setStyleSheet(u"color: white;")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 581, 61))
        self.label_7.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_7.setScaledContents(False)
        self.ppm = QLabel(self.tab)
        self.ppm.setObjectName(u"ppm")
        self.ppm.setGeometry(QRect(260, 140, 71, 71))
        font = QFont()
        font.setPointSize(20)
        self.ppm.setFont(font)
        self.ppm.setStyleSheet(u"color: white;")
        self.ppm.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 240, 101, 16))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: white;")
        self.resultado = QLabel(self.tab)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(320, 240, 161, 16))
        self.resultado.setStyleSheet(u"color: white;")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(330, 170, 31, 16))
        self.label_13.setStyleSheet(u"color: white;")
        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 60, 581, 251))
        self.label_16.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_16.setScaledContents(False)
        self.guardar_resultado = QPushButton(self.tab)
        self.guardar_resultado.setObjectName(u"guardar_resultado")
        self.guardar_resultado.setGeometry(QRect(240, 273, 111, 31))
        self.guardar_resultado.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.tabWidget.addTab(self.tab, "")
        self.label_16.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.ppm.raise_()
        self.label_11.raise_()
        self.resultado.raise_()
        self.label_13.raise_()
        self.guardar_resultado.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, -1, 581, 311))
        self.label_4.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_4.setScaledContents(False)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 50, 281, 20))
        self.label_6.setStyleSheet(u"color:white;")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 180, 75, 16))
        self.label_14.setStyleSheet(u"color: white;")
        self.enviar = QPushButton(self.tab_2)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setGeometry(QRect(390, 260, 91, 24))
        self.enviar.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.placa_envio = QLineEdit(self.tab_2)
        self.placa_envio.setObjectName(u"placa_envio")
        self.placa_envio.setGeometry(QRect(380, 220, 113, 24))
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(50, 110, 291, 181))
        self.label_15.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_15.setScaledContents(True)
        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(380, 110, 91, 16))
        self.label_23.setStyleSheet(u"color: white;")
        self.id_oficina_envio = QLineEdit(self.tab_2)
        self.id_oficina_envio.setObjectName(u"id_oficina_envio")
        self.id_oficina_envio.setGeometry(QRect(380, 140, 113, 24))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 581, 311))
        self.label_3.setPixmap(QPixmap(u"assets/material-design-wallpaper-10.png"))
        self.label_3.setScaledContents(True)
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 20, 311, 20))
        self.label_9.setStyleSheet(u"color:white;")
        self.label_28 = QLabel(self.tab_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(100, 70, 91, 16))
        self.label_28.setStyleSheet(u"color: white;")
        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(300, 70, 91, 16))
        self.label_29.setStyleSheet(u"color: white;")
        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(300, 130, 91, 16))
        self.label_30.setStyleSheet(u"color: white;")
        self.label_31 = QLabel(self.tab_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(100, 200, 131, 16))
        self.label_31.setStyleSheet(u"color: white;")
        self.label_32 = QLabel(self.tab_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(100, 130, 121, 16))
        self.label_32.setStyleSheet(u"color: white;")
        self.label_33 = QLabel(self.tab_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(300, 200, 161, 16))
        self.label_33.setStyleSheet(u"color: white;")
        self.cedula = QLineEdit(self.tab_5)
        self.cedula.setObjectName(u"cedula")
        self.cedula.setGeometry(QRect(100, 90, 113, 24))
        self.f_nacimiento = QLineEdit(self.tab_5)
        self.f_nacimiento.setObjectName(u"f_nacimiento")
        self.f_nacimiento.setGeometry(QRect(300, 220, 113, 24))
        self.apellido = QLineEdit(self.tab_5)
        self.apellido.setObjectName(u"apellido")
        self.apellido.setGeometry(QRect(300, 160, 113, 24))
        self.s_nombre = QLineEdit(self.tab_5)
        self.s_nombre.setObjectName(u"s_nombre")
        self.s_nombre.setGeometry(QRect(100, 160, 113, 24))
        self.nombre = QLineEdit(self.tab_5)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(300, 90, 113, 24))
        self.s_apellido = QLineEdit(self.tab_5)
        self.s_apellido.setObjectName(u"s_apellido")
        self.s_apellido.setGeometry(QRect(100, 220, 113, 24))
        self.r_propietario = QPushButton(self.tab_5)
        self.r_propietario.setObjectName(u"r_propietario")
        self.r_propietario.setGeometry(QRect(250, 270, 91, 24))
        self.r_propietario.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.label_38 = QLabel(self.tab_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(430, 60, 91, 16))
        self.label_38.setStyleSheet(u"color: white;")
        self.contra = QLineEdit(self.tab_5)
        self.contra.setObjectName(u"contra")
        self.contra.setGeometry(QRect(430, 90, 113, 24))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_8 = QLabel(self.tab_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 581, 311))
        self.label_8.setPixmap(QPixmap(u"assets/material-design-wallpaper-10.png"))
        self.label_8.setScaledContents(True)
        self.label_34 = QLabel(self.tab_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(230, 60, 91, 16))
        self.label_34.setStyleSheet(u"color: white;")
        self.label_35 = QLabel(self.tab_6)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(230, 200, 151, 16))
        self.label_35.setStyleSheet(u"color: white;")
        self.label_36 = QLabel(self.tab_6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 130, 61, 20))
        self.label_36.setStyleSheet(u"color: white;")
        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 20, 311, 20))
        self.label_10.setStyleSheet(u"color:white;")
        self.placa_registrar = QLineEdit(self.tab_6)
        self.placa_registrar.setObjectName(u"placa_registrar")
        self.placa_registrar.setGeometry(QRect(230, 90, 113, 24))
        self.modelo_registrar = QLineEdit(self.tab_6)
        self.modelo_registrar.setObjectName(u"modelo_registrar")
        self.modelo_registrar.setGeometry(QRect(230, 160, 113, 24))
        self.cedula_moto_registrar = QLineEdit(self.tab_6)
        self.cedula_moto_registrar.setObjectName(u"cedula_moto_registrar")
        self.cedula_moto_registrar.setGeometry(QRect(230, 230, 113, 24))
        self.r_propietario_2 = QPushButton(self.tab_6)
        self.r_propietario_2.setObjectName(u"r_propietario_2")
        self.r_propietario_2.setGeometry(QRect(240, 280, 91, 24))
        self.r_propietario_2.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 581, 311))
        self.label_18.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_18.setScaledContents(False)
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(210, 10, 141, 20))
        self.label_19.setStyleSheet(u"color:white;")
        self.guardar_datos_oficina = QPushButton(self.tab_3)
        self.guardar_datos_oficina.setObjectName(u"guardar_datos_oficina")
        self.guardar_datos_oficina.setGeometry(QRect(220, 270, 91, 24))
        self.guardar_datos_oficina.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(210, 130, 75, 16))
        self.label_20.setStyleSheet(u"color: white;")
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(210, 50, 91, 16))
        self.label_21.setStyleSheet(u"color: white;")
        self.guardar_ciudad = QLineEdit(self.tab_3)
        self.guardar_ciudad.setObjectName(u"guardar_ciudad")
        self.guardar_ciudad.setGeometry(QRect(210, 150, 113, 24))
        self.guardar_oficina = QLineEdit(self.tab_3)
        self.guardar_oficina.setObjectName(u"guardar_oficina")
        self.guardar_oficina.setGeometry(QRect(210, 80, 113, 24))
        self.label_37 = QLabel(self.tab_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(210, 190, 75, 16))
        self.label_37.setStyleSheet(u"color: white;")
        self.guardar_nombre = QLineEdit(self.tab_3)
        self.guardar_nombre.setObjectName(u"guardar_nombre")
        self.guardar_nombre.setGeometry(QRect(210, 210, 113, 24))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_22 = QLabel(self.tab_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 0, 581, 311))
        self.label_22.setPixmap(QPixmap(u"assets/material-design-wallpaper-2.png"))
        self.label_22.setScaledContents(False)
        self.label_24 = QLabel(self.tab_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(210, 30, 141, 20))
        self.label_24.setStyleSheet(u"color:white;")
        self.label_25 = QLabel(self.tab_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(210, 80, 91, 16))
        self.label_25.setStyleSheet(u"color: white;")
        self.registrar_oficina_id = QLineEdit(self.tab_4)
        self.registrar_oficina_id.setObjectName(u"registrar_oficina_id")
        self.registrar_oficina_id.setGeometry(QRect(210, 100, 113, 24))
        self.label_26 = QLabel(self.tab_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(210, 140, 75, 16))
        self.label_26.setStyleSheet(u"color: white;")
        self.registrar_ciudad_oficina = QLineEdit(self.tab_4)
        self.registrar_ciudad_oficina.setObjectName(u"registrar_ciudad_oficina")
        self.registrar_ciudad_oficina.setGeometry(QRect(210, 160, 113, 24))
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(210, 200, 75, 16))
        self.label_27.setStyleSheet(u"color: white;")
        self.registrar_nombre_oficina = QLineEdit(self.tab_4)
        self.registrar_nombre_oficina.setObjectName(u"registrar_nombre_oficina")
        self.registrar_nombre_oficina.setGeometry(QRect(210, 230, 113, 24))
        self.registrar_oficina = QPushButton(self.tab_4)
        self.registrar_oficina.setObjectName(u"registrar_oficina")
        self.registrar_oficina.setGeometry(QRect(220, 270, 91, 24))
        self.registrar_oficina.setStyleSheet(u"background-color:teal; border-radius:0; color:white;")
        self.tabWidget.addTab(self.tab_4, "")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 40, 171, 31))
        font2 = QFont()
        font2.setFamily(u"Ubuntu Mono")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        Mq.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Mq)
        self.statusbar.setObjectName(u"statusbar")
        Mq.setStatusBar(self.statusbar)

        self.retranslateUi(Mq)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Mq)
    # setupUi

    def retranslateUi(self, Mq):
        Mq.setWindowTitle(QCoreApplication.translate("Mq", u"MainWindow", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("Mq", u"RESULTADOS DE PRUEBA DE CO", None))
        self.label_7.setText("")
        self.ppm.setText(QCoreApplication.translate("Mq", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Mq", u"RESULTADO", None))
        self.resultado.setText(QCoreApplication.translate("Mq", u".........", None))
        self.label_13.setText(QCoreApplication.translate("Mq", u"ppm", None))
        self.label_16.setText("")
        self.guardar_resultado.setText(QCoreApplication.translate("Mq", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Mq", u"Prueba", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("Mq", u"FORMULARIO DE ENV\u00cdO  DE RESULTADO", None))
        self.label_14.setText(QCoreApplication.translate("Mq", u"Placa", None))
        self.enviar.setText(QCoreApplication.translate("Mq", u"Enviar", None))
        self.label_15.setText("")
        self.label_23.setText(QCoreApplication.translate("Mq", u"Id Oficina", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Mq", u"Env\u00edo", None))
        self.label_3.setText("")
        self.label_9.setText(QCoreApplication.translate("Mq", u"FORMULARIO DE REGISTRO DE PROPIETARIO", None))
        self.label_28.setText(QCoreApplication.translate("Mq", u"CEDULA", None))
        self.label_29.setText(QCoreApplication.translate("Mq", u"NOMBRE", None))
        self.label_30.setText(QCoreApplication.translate("Mq", u"APELLIDO", None))
        self.label_31.setText(QCoreApplication.translate("Mq", u"SEGUNDO APELLIDO", None))
        self.label_32.setText(QCoreApplication.translate("Mq", u"SEGUNDO NOMBRE", None))
        self.label_33.setText(QCoreApplication.translate("Mq", u"F.NACIMIENTO", None))
        self.r_propietario.setText(QCoreApplication.translate("Mq", u"Registrar", None))
        self.label_38.setText(QCoreApplication.translate("Mq", u"CONTRASE\u00d1A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Mq", u"Propietario", None))
        self.label_8.setText("")
        self.label_34.setText(QCoreApplication.translate("Mq", u"PLACA", None))
        self.label_35.setText(QCoreApplication.translate("Mq", u"CEDULA PROPIETARIO", None))
        self.label_36.setText(QCoreApplication.translate("Mq", u"MODELO", None))
        self.label_10.setText(QCoreApplication.translate("Mq", u"FORMULARIO DE REGISTRO DE MOTOCICLETA", None))
        self.cedula_moto_registrar.setText("")
        self.r_propietario_2.setText(QCoreApplication.translate("Mq", u"Registrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Mq", u"Motocicleta", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("Mq", u"DATOS DE OFICINA", None))
        self.guardar_datos_oficina.setText(QCoreApplication.translate("Mq", u"Guardar", None))
        self.label_20.setText(QCoreApplication.translate("Mq", u"Ciudad", None))
        self.label_21.setText(QCoreApplication.translate("Mq", u"Id Oficina", None))
        self.label_37.setText(QCoreApplication.translate("Mq", u"Nombre", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Mq", u"Oficina", None))
        self.label_22.setText("")
        self.label_24.setText(QCoreApplication.translate("Mq", u"REGISTRAR OFICINA", None))
        self.label_25.setText(QCoreApplication.translate("Mq", u"Id Oficina", None))
        self.label_26.setText(QCoreApplication.translate("Mq", u"Ciudad", None))
        self.label_27.setText(QCoreApplication.translate("Mq", u"Nombre", None))
        self.registrar_oficina.setText(QCoreApplication.translate("Mq", u"Registrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Mq", u"R.Oficina", None))
        self.label_2.setText(QCoreApplication.translate("Mq", u"Prueba de CO", None))
    # retranslateUi

