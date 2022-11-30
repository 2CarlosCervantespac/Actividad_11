from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QLabel
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from lista import Lista
from particula import Particula
from algoritmos import distancia_euclidiana
from lista import Punto

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.lista = Lista()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label = QLabel()
        self.ui.statusbar.addWidget(self.label)
        #conexion con los botones de la interfaz
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
   
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        #Dibujar y limpiar
        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)
        
        self.puntos = []
        self.puntos_cercanos = []
        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionPuntos_mas_Cercanos.triggered.connect(self.calcular_puntos_mas_cercanos)
        self.actualizar_particulas()

    #Funcion puntos cercanos
    @Slot()
    def calcular_puntos_mas_cercanos(self):
        for punto01 in self.puntos:
            distMin = 1000
            punto = Punto()
            for todos in self.puntos:
                if punto01 == todos:
                    continue
                dist = distancia_euclidiana(punto01.x, punto01.y, todos.x, todos.y)
                if dist < distMin:
                    distMin = dist
                    punto = todos
            self.puntos_cercanos.append([punto01, punto])
        self.dibujar_puntos_mas_cercanos()

    
    def dibujar_puntos_mas_cercanos(self):
        for punto01, punto02 in self.puntos_cercanos:
            pen = QPen()
            color = QColor(punto01.red, punto01.green, punto01.blue)
            pen.setColor(color)
            self.scene.addLine(punto01.x, punto01.y, punto02.x, punto02.y, pen)

    #Funcion actualizar
    @Slot()
    def actualizar_particulas(self):
        self.label.setText(f"Particulas: {self.lista.cantidad()}")    
    #Funcion para dibujar los puntos conectada con el trigger
    @Slot()
    def dibujar_puntos(self):
        """pen = QPen()
        pen.setWidth(2)

        for particula in self.lista:
            r = particula.red
            g = particula.blue
            b = particula.green
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)"""
        self.puntos = self.lista.get_puntos()
        for punto in self.puntos:
            x = punto.x
            y = punto.y
            red = punto.red
            green = punto.green
            blue = punto.blue
            color = QColor(red, green, blue)
            pen = QPen()
            pen.setWidth(2)
            pen.setColor(color)

            self.scene.addEllipse(x, y, 5, 5, pen)
        

    #Funcion para hacer zoom en el Qescene con el scroll del mouse 
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    #funciones ordenar
    @Slot()
    def ordenar_id(self):
        self.lista.sort_id()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.lista))

    @Slot()
    def ordenar_distancia(self):
        self.lista.sort_distancia()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.lista))

    @Slot()
    def ordenar_velocidad(self):
        self.lista.sort_velocidad()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.lista))

    #Funcion para dibujar las particulas
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.lista:
            r = particula.red
            g = particula.blue
            b = particula.green
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)
            self.scene.addLine(particula.origen_x+3, particula.origen_y+3, particula.destino_x, particula.destino_y, pen)
    #Funcion para limpiar las particulas en el Qescene 
    @Slot()
    def limpiar(self):
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.lista:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
                
                self.ui.tabla.setItem(0, 0, QTableWidgetItem(particula.id))
                self.ui.tabla.setItem(0, 1, QTableWidgetItem(str(particula.origen_x)))
                self.ui.tabla.setItem(0, 2, QTableWidgetItem(str(particula.origen_y)))
                self.ui.tabla.setItem(0, 3, QTableWidgetItem(str(particula.destino_x)))
                self.ui.tabla.setItem(0, 4, QTableWidgetItem(str(particula.destino_y)))
                self.ui.tabla.setItem(0, 5, QTableWidgetItem(str(particula.velocidad)))
                self.ui.tabla.setItem(0, 6, QTableWidgetItem(str(particula.red)))
                self.ui.tabla.setItem(0, 7, QTableWidgetItem(str(particula.green)))
                self.ui.tabla.setItem(0, 8, QTableWidgetItem(str(particula.blue)))
                self.ui.tabla.setItem(0, 9, QTableWidgetItem(str(particula.distancia)))

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con el Id "{id}" no fue encontrada'
            )



    @Slot()
    def mostar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.lista))

        row = 0
        for particula in self.lista:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)
            
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.lista.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def click_mostrar(self):
        #self.lista.mostar()
        self.ui.salida.clear()        
        self.ui.salida.insertPlainText(str(self.lista))

    @Slot()
    def click_agregar(self):
        id = self.ui.Id_lineEdit.text()
        origen_x = self.ui.Origen_X_spinBox.value()
        origen_y = self.ui.Origen_Y_spinBox.value()
        destino_x = self.ui.Destino_X_spinBox.value()
        destino_y = self.ui.Destino_Y_spinBox.value()
        velocidad = self.ui.Velocidad_spinBox.value()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()
        #distancia = self.ui.distancia_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista.agregar_final(particula)
    
        #print(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue,distancia)
        #self.ui.salida.insertPlainText(id + str(origen_x) + str(origen_y) + str(destino_x) + str(destino_y) + str(velocidad) + str(red) + str(green) + str(blue) + str(distancia))
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.Id_lineEdit.text()
        origen_x = self.ui.Origen_X_spinBox.value()
        origen_y = self.ui.Origen_Y_spinBox.value()
        destino_x = self.ui.Destino_X_spinBox.value()
        destino_y = self.ui.Destino_Y_spinBox.value()
        velocidad = self.ui.Velocidad_spinBox.value()
        red = self.ui.Red_spinBox.value()
        green = self.ui.Green_spinBox.value()
        blue = self.ui.Blue_spinBox.value()
        #distancia = self.ui.distancia_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista.agregar_inicio(particula)
