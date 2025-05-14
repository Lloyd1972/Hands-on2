from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QAbstractItemDelegate, QMessageBox
from PySide6.QtCore import Slot, Qt
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np
import random

X = np.array([23, 26, 30, 34, 43, 48, 52, 57, 58])
Y = np.array([651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518])

class MainWindow(QMainWindow):
    def __init__(self):
        # Llamamos al constructor de la clase base (MainWindow) utilizando super()
        super(MainWindow, self).__init__()
        
        # Instancia la interfaz de usuario definida en Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # Configura la interfaz de usuario en la ventana
        
        fig = Figure()
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar2QT(self.canvas, self)
        
        self.ui.gridLayout_2.removeWidget(self.ui.resultsLabel)
        
        self.ui.gridLayout_2.addWidget(self.canvas)
        self.ui.gridLayout_2.addWidget(toolbar)
        self.ui.gridLayout_2.addWidget(self.ui.resultsLabel)
        
        for row in range(self.ui.ownValuesTable.rowCount()):
            self.ui.ownValuesTable.item(row, 0).setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        
        self.initialLinregress()
        self.randomize()
        
        self.ui.ownValuesTable.cellDoubleClicked.connect(self.openEditor)
        self.ui.ownValuesTable.closeEditor = self.closeEditorHandler
        self.ui.generateAdvertising.clicked.connect(self.randomize)

    def randomize(self):
        start = self.ui.minRange.value()
        finish = self.ui.maxRange.value()
        
        for r in range(self.ui.ownValuesTable.rowCount()):
            self.ui.ownValuesTable.setItem(r, 1, QTableWidgetItem(f"{random.randint(start, finish)}"))
        self.linregress()
        
    def initialLinregress(self):
        ## PROMEDIOS DE X y Y
        x_bar, y_bar = np.mean(X), np.mean(Y)
        
        ## BETA 1
        beta_1_num = ((X - x_bar) * (Y - x_bar)).sum()
        denom_beta_1 = ((X - x_bar)**2).sum()
        self.beta_1 = beta_1_num / denom_beta_1
        
        ## BETA 0
        self.beta_0 = y_bar - (self.beta_1 * x_bar)
        
        self.ui.resultsLabel.setText(f"β₁ = {str(self.beta_1)}, β₀ = {str(self.beta_0)}")
        
    def _fmt(self, x: float):
        return f"{x:,.4f}"
        
    def linregress(self):
        xv, yv, steps = [], [], []
        subindexes = ["₁", "₂", "₃", "₄", "₅"]
        for r, sub in enumerate(subindexes):
            txt = self.ui.ownValuesTable.item(r, 1).text().replace(",", "")
            
            if not txt:
                continue
            xi = float(txt)
            if xi.is_integer():
                xi = int(xi)
            y_circumflex = self.beta_0 + self.beta_1 * xi
            
            xv.append(xi); yv.append(y_circumflex)
            
            steps.append("")
            steps.append("ŷᵢ = β₀ + β₁xᵢ")
            steps.append(f"ŷ{sub} = {self._fmt(self.beta_0)} + ({self._fmt(self.beta_1)} * {xi:,})")
            steps.append(f"ŷ{sub} = {self._fmt(self.beta_0)} + {self._fmt(self.beta_1 * xi)}")
            steps.append(f"ŷ{sub} = {self._fmt(y_circumflex)}")
            self.ui.ownValuesTable.setItem(r, 0, QTableWidgetItem(str(self._fmt(y_circumflex))))
        self.ui.ownValuesTable.resizeColumnsToContents()
        
        pairs = sorted(zip(np.concatenate((X, xv)),
                      np.concatenate(((self.beta_0 + self.beta_1 * X), yv))))
        xs, ys = map(np.array, zip(*pairs))
        
        self.ax.clear()
        self.ax.set_title('Caso Benetton', fontsize=20)
        self.ax.set_xlabel('Advertising (Million Euro)')
        self.ax.set_ylabel('Sales (Million Euro)')
        self.ax.plot(xs, ys)
        self.ax.scatter(X, Y, c='#32CD32')
        self.ax.scatter(xv, yv, c='#00b2ee')
        self.ax.grid()
        self.canvas.draw_idle()
        
    @Slot()
    def openEditor(self):
        curRow, curCol = self.ui.ownValuesTable.currentRow(), self.ui.ownValuesTable.currentColumn()
        curItem = self.ui.ownValuesTable.item(curRow, curCol)
        
        if Qt.ItemFlag.ItemIsEditable in curItem.flags():
            for row in range(self.ui.ownValuesTable.rowCount()):
                if row == curRow:
                    continue
                self.ui.ownValuesTable.item(row, 1).setFlags(Qt.ItemFlag.ItemIsSelectable|Qt.ItemFlag.ItemIsEnabled)
        
    def closeEditorHandler(self, editor: QWidget, hint: QAbstractItemDelegate.EndEditHint):
        if hint == QAbstractItemDelegate.EndEditHint.EditNextItem:
            return
        
        curRow, curCol = self.ui.ownValuesTable.currentRow(), self.ui.ownValuesTable.currentColumn()
        curItem = self.ui.ownValuesTable.item(curRow, curCol)
        text = curItem.text()
        
        try:
            if "," in text:
                text = text.replace(",", "")
            
            value = float(text)
            if value.is_integer():
                value = int(value)
        except ValueError:
            if hint != QAbstractItemDelegate.EndEditHint.NoHint:
                QMessageBox.critical(self, "Error", "¡Por favor, ingrese solo valores numéricos!")
                curItem.setText("")
            return
        
        if value < 0:
            if hint != QAbstractItemDelegate.EndEditHint.NoHint:
                QMessageBox.warning(self, "Error", "¡Por favor, ingrese un número mayor o igual a 0!")
                curItem.setText("")
            return
        
        curItem.setText(f"{value:,}")
        
        if hint in [QAbstractItemDelegate.EndEditHint.SubmitModelCache, QAbstractItemDelegate.EndEditHint.NoHint]:
            if not self.ui.ownValuesTable.isPersistentEditorOpen(curItem):
                return
            
            for row in range(self.ui.ownValuesTable.rowCount()):
                self.ui.ownValuesTable.item(row, 1).setFlags(Qt.ItemFlag.ItemIsSelectable|Qt.ItemFlag.ItemIsEnabled|Qt.ItemFlag.ItemIsEditable)
            QTableWidget.closeEditor(self.ui.ownValuesTable, editor, hint) # Cierra el editor
            self.linregress()
        elif hint == QAbstractItemDelegate.EndEditHint.RevertModelCache:
            # Comprueba si el usuario ha revertido la caché del modelo
            for row in range(self.ui.ownValuesTable.rowCount()):
                self.ui.ownValuesTable.item(row, 1).setFlags(Qt.ItemFlag.ItemIsSelectable|Qt.ItemFlag.ItemIsEnabled|Qt.ItemFlag.ItemIsEditable)
            QTableWidget.closeEditor(self.ui.ownValuesTable, editor, hint) # Cierra el editor