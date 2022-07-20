import sys
import mysql.connector
from datetime import date
import sys, serial, time, json, math, modulo
import PySide2

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPen)
from PySide2.QtWidgets import *

# IMPORT PYSIDE2EXTN WIDGET YOU USED IN THE QTDESIGNER FOR DESIGNING.
from PySide2extn.RoundProgressBar import roundProgressBar

# UI FILE CONVERTED FROM .ui to python file ui.py
from ui_mainwindow import *


class MainWindow(QMainWindow):
   
    # Importing primary sensors
    def intReady(self, ppmv):
        self.ppmv = ppmv
        # Imported from worker vars
        #self.ui.ppm.rpb_textValue = str(1000)
        self.ui.ppm.setText(str(ppmv))

        if (self.ppmv < 1500):
            print(self.ppmv)
            self.ui.resultado.setText("Inf al 3%");
            self.resultado = "Menor al 3%"

        self.ppmv = int(self.ui.ppm.text())

        if (int(self.ppmv) > 1500):
            print(self.ppmv)
            self.ui.resultado.setText("Sup al 3%");
            self.resultado = "Mayor al 3%"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Mq()
        self.ui.setupUi(self)


        # 1 - create Worker and Thread inside the Form
        self.obj = modulo.Worker()  # no parent!
        self.thread = PySide2.QtCore.QThread()  # no parent!

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.obj.intReady.connect(self.intReady)


        # 3 - Move the Worker object to the Thread object
        self.obj.moveToThread(self.thread)

        # 4 - Connect Worker Signals to the Thread slots
        self.obj.finished.connect(self.thread.quit)

        # 5 - Connect Thread started signal to Worker operational slot method

        self.thread.started.connect(self.obj.procCounter)

        # * - Thread finished signal will close the app if you want!
        # self.thread.finished.connect(app.exit)

        # 6 - Start the thread
        self.thread.start()

        #self.onIntReady(self)

        self.resultado = ""

        self.ppmv = int(self.ui.ppm.text())

        #self.ui.ppm.setText(str(self.ppm))

        self.resultado_guardado = ""
        self.pp_guardado = ""

        # Enviar registro
        self.ui.enviar.clicked.connect(self.enviar_registro)

        # Guardar datos de oficina
        self.ui.guardar_datos_oficina.clicked.connect(self.guardar_oficina_tab)

        # Registrar nueva oficina
        self.ui.registrar_oficina.clicked.connect(self.registrar_oficina_tab)

        # Registrar nueva motocicleta
        self.ui.r_propietario_2.clicked.connect(self.registrar_motocicleta_tab)

        # Registrar nuevo propietario
        self.ui.r_propietario.clicked.connect(self.registrar_propietario_tab)

        # Guardar datos de mediciones
        self.ui.guardar_resultado.clicked.connect(self.guardar_resultados)

    def guardar_resultados(self):

        # Almaceno en variables globales

        self.ppm_guardado = self.ui.ppm.text()

        self.resultado_guardado = self.ui.resultado.text()

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Correcto!")
        dlg.setText("Los datos han sido guardados en memoria para su envío")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")

    def guardar_oficina_tab(self):

        # Almaceno en variables globales

        self.guardar_id_oficina = self.ui.guardar_oficina.text()

        self.guardar_ciudad_oficina = self.ui.guardar_ciudad.text()

        self.guardar_nombre_oficina = self.ui.guardar_nombre.text()

        # El formulario queda rellenado con esos datos

        self.ui.id_oficina_envio.setText(self.guardar_id_oficina);

        self.ui.guardar_ciudad.setText(self.guardar_ciudad_oficina);

        self.ui.guardar_nombre.setText(self.guardar_nombre_oficina);

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Correcto!")
        dlg.setText("Los datos de la oficina han sido guardados y rellenados en los campos")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")

    def registrar_oficina_tab(self):

        id_oficina = int(self.ui.registrar_oficina_id.text())

        ciudad_oficina = str(self.ui.registrar_ciudad_oficina.text())

        nombre_oficina = str(self.ui.registrar_nombre_oficina.text())

        try:
            connection = mysql.connector.connect(host='localhost', database='moto', user='root', password='')

            mySql_insert_query = """INSERT INTO Oficina ( idOficina, d_ubicacion, nombre )
                                   VALUES 
                                   (%s, %s, %s) """

            record = (id_oficina, ciudad_oficina, nombre_oficina )

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Los datos de registro se han ennviado correctamente")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

            cursor.close()

            self.ui.registrar_oficina_id.setText("")
            self.ui.registrar_ciudad_oficina.setText("")
            self.ui.registrar_nombre_oficina.setText("")



        except mysql.connector.Error as error:
            print("Failed to insert record into table {}".format(error))
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Error al enviar los datos, revise nuevamente")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

        finally:
            connection
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    def registrar_motocicleta_tab(self):

        placa_registrar = str(self.ui.placa_registrar.text())

        modelo_registrar = str(self.ui.modelo_registrar.text())

        cedula_registrar = int(self.ui.cedula_moto_registrar.text())

        try:
            connection = mysql.connector.connect(host='localhost', database='moto', user='root', password='')

            mySql_insert_query = """INSERT INTO Motocicleta ( placa, modelo, Propietario_cedula )
                                               VALUES 
                                               (%s, %s, %s) """

            record = (placa_registrar, modelo_registrar, cedula_registrar)

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Los datos de registro se han ennviado correctamente a su cédula")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

            cursor.close()

            self.ui.placa_registrar.setText("")
            self.ui.modelo_registrar.setText("")
            self.ui.cedula_moto_registrar.setText("")

        except mysql.connector.Error as error:
            print("Failed to insert record into table {}".format(error))
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Error al enviar los datos, revise nuevamente")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    def registrar_propietario_tab(self):

        cedula = int(self.ui.cedula.text())

        nombre = str(self.ui.nombre.text())

        s_nombre = str(self.ui.s_nombre.text())

        apellido = str(self.ui.apellido.text())

        s_apellido = str(self.ui.s_apellido.text())

        f_nacimiento = str(self.ui.f_nacimiento.text())

        contraseña = str(self.ui.contra.text())

        try:
            connection = mysql.connector.connect(host='localhost', database='moto', user='root', password='')

            mySql_insert_query = """INSERT INTO Propietario ( cedula, nombre, s_nombre, apellido, s_apellido, f_nacimiento, contra )
                                               VALUES 
                                               (%s, %s, %s, %s, %s, %s, %s) """

            record = (cedula, nombre, s_nombre, apellido, s_apellido, f_nacimiento, contraseña)

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Los datos de registro se han ennviado correctamente a su cédula")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

            cursor.close()

            self.ui.cedula.setText("")
            self.ui.nombre.setText("")
            self.ui.s_nombre.setText("")
            self.ui.apellido.setText("")
            self.ui.s_apellido.setText("")
            self.ui.f_nacimiento.setText("")
            self.ui.contra.setText("")



        except mysql.connector.Error as error:

            print("Failed to insert record into table {}".format(error))
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Error al enviar los datos, revise nuevamente")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    def enviar_registro(self):

        id_oficina = int(self.ui.id_oficina_envio.text())

        placa_motocicleta = str(self.ui.placa_envio.text())

        hoy = str(date.today())

        try:
            connection = mysql.connector.connect(host='localhost', database='moto', user='root', password='')

            mySql_insert_query = """INSERT INTO Prueba ( f_prueba, resultado, p_dioxido, Motocicleta_placa, Oficina_idOficina )
                                               VALUES 
                                               (%s, %s, %s, %s, %s) """

            record = (hoy, self.resultado_guardado, int(self.ppm_guardado), placa_motocicleta, id_oficina)

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Los datos de registro se han ennviado correctamente a su cédula")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

            cursor.close()

            self.ui.placa_envio.setText("")


        except mysql.connector.Error as error:
            print("Failed to insert record into table {}".format(error))
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Error!")
            dlg.setText("Error al enviar los datos, revise nuevamente")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

