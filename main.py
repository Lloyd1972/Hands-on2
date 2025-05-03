# Importa las clases necesarias de PySide6
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QPalette, QColor
from mainwindow import MainWindow # Importa la clase MainWindow desde el archivo mainwindow.py
import sys # Importa el módulo sys

# Crea una instancia de QApplication
app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create('fusion')) # Establece el estilo de la aplicación como Fusion

# Crea una paleta de colores basada en el estilo Windows Vista
palette = QStyleFactory.create('windowsvista').standardPalette()
# Cambia el color de resaltado en la paleta
palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Highlight, QColor("#0078D7"))

# Establece la paleta personalizada en la aplicación
app.setPalette(palette)

# Crea una instancia de la ventana principal (MainWindow)
window = MainWindow()
window.show() # Muestra la ventana principal

sys.exit(app.exec()) # Ejecuta la aplicación y espera a que se cierre