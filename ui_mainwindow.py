# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 503)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionPuntos_mas_Cercanos = QAction(MainWindow)
        self.actionPuntos_mas_Cercanos.setObjectName(u"actionPuntos_mas_Cercanos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(500)

        self.gridLayout_6.addWidget(self.Velocidad_spinBox, 7, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout_6.addWidget(self.agregar_final_pushButton, 12, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.Origen_X_spinBox = QSpinBox(self.groupBox_2)
        self.Origen_X_spinBox.setObjectName(u"Origen_X_spinBox")
        self.Origen_X_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_X_spinBox, 0, 1, 1, 1)

        self.Origen_Y_spinBox = QSpinBox(self.groupBox_2)
        self.Origen_Y_spinBox.setObjectName(u"Origen_Y_spinBox")
        self.Origen_Y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_Y_spinBox, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 7, 0, 1, 1)

        self.Id_lineEdit = QLineEdit(self.groupBox)
        self.Id_lineEdit.setObjectName(u"Id_lineEdit")

        self.gridLayout_6.addWidget(self.Id_lineEdit, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.Red_spinBox = QSpinBox(self.groupBox_4)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.Red_spinBox)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.Green_spinBox = QSpinBox(self.groupBox_4)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.Green_spinBox)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.Blue_spinBox = QSpinBox(self.groupBox_4)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.horizontalLayout.addWidget(self.Blue_spinBox)


        self.gridLayout_6.addWidget(self.groupBox_4, 6, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.Destino_X_spinBox = QSpinBox(self.groupBox_3)
        self.Destino_X_spinBox.setObjectName(u"Destino_X_spinBox")
        self.Destino_X_spinBox.setMaximum(500)

        self.gridLayout_7.addWidget(self.Destino_X_spinBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 2, 1, 1)

        self.Destino_Y_spinBox = QSpinBox(self.groupBox_3)
        self.Destino_Y_spinBox.setObjectName(u"Destino_Y_spinBox")
        self.Destino_Y_spinBox.setMaximum(500)

        self.gridLayout_7.addWidget(self.Destino_Y_spinBox, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 5, 0, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_6.addWidget(self.agregar_inicio_pushButton, 11, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.salida = QPlainTextEdit(self.groupBox_5)
        self.salida.setObjectName(u"salida")

        self.verticalLayout.addWidget(self.salida)

        self.mostrar_pushButton = QPushButton(self.groupBox_5)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.verticalLayout.addWidget(self.mostrar_pushButton)

        self.ordenar_id_pushButton = QPushButton(self.groupBox_5)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")

        self.verticalLayout.addWidget(self.ordenar_id_pushButton)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox_5)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.verticalLayout.addWidget(self.ordenar_distancia_pushButton)

        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox_5)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.verticalLayout.addWidget(self.ordenar_velocidad_pushButton)


        self.gridLayout_3.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 2, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_5.addWidget(self.dibujar, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 599, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName(u"menuVista")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuVista.addAction(self.actionPuntos)
        self.menuAlgoritmos.addAction(self.actionPuntos_mas_Cercanos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionPuntos_mas_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos mas Cercanos", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" X:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Id", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Distancia", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar Velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVista.setTitle(QCoreApplication.translate("MainWindow", u"Vista", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

